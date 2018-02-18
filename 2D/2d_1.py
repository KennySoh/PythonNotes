from libdw import sm
import os
import glob
import time
import RPi.GPIO as GPIO


###           CONFIGURING THE TEMPERATURE SENSOR               ###

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


###           DEFINING AND SETTING THE GPIO PINS               ###

GPIO.setmode(GPIO.BCM)

pwm_pin = 18
in1_pin = 23
in2_pin = 24
#fan_pin = ##

GPIO.setup(pwm_pin, GPIO.OUT)
GPIO.setup(in1_pin, GPIO.OUT)
GPIO.setup(in2_pin, GPIO.OUT)

p = GPIO.PWM(pwm_pin, 200) #instantiate PWM instance
#f = GPIO.PWM(fan_pin, 200)

###           FUNCTIONS                  ###

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp = float(temp_string) / 1000.0
        return temp

        
class Controller(sm.SM):
    state=0
    def getNextValues(self,state,inp):
        if state == 0 and inp[0] < desired_temp:
            nextState = 0
            return (nextState,(0,0))
        elif state == 0 and inp[0] >= desired_temp:
            nextState = 1
            ########## PID CONTROLLER##############
            Kp=[1,1]### Adjust
            Kd=[-0.1,-0.1]##### 
            pwm_fan=Kp[0]*(inp[1])+Kd[0]*(inp[2])
            pwm_pump=Kp[1]*(inp[1])+Kd[1]*(inp[2])
            #####limit pwm Between 0 to 100 duty cycle#####
            if pwm_fan>100:
                pwm_fan=100
            if pwm_fan<0:
                pwm_fan=0                  
            if pwm_pump>100:
                pwm_pump=100
            if pwm_pump<0:
                pwm_pump=0
            return (nextState,(pwm_fan,pwm_pump))
        elif state == 1 and inp[0] < desired_temp:
            nextState = 0
            return (nextState,(0,0))
        elif state == 1 and inp[0] >= desired_temp:
            nextState = 1
            Kp=[1,1]
            Kd=[-0.1,-0.1]
            pwm_fan=Kp[0]*(inp[1])+Kd[0]*(inp[2])
            pwm_pump=Kp[1]*(inp[1])+Kd[1]*(inp[2])
            #####limit pwm Between 0 to 100 duty cycle#####
            if pwm_fan>100:
                pwm_fan=100
            if pwm_fan<0:
                pwm_fan=0                  
            if pwm_pump>100:
                pwm_pump=100
            if pwm_pump<0:
                pwm_pump=0
            return (nextState,(pwm_fan,pwm_pump))

                     
def clockwise():
    #GPIO.output(in1_pin, True)    
    #GPIO.output(in2_pin, False)

 
def counter_clockwise():
    #GPIO.output(in1_pin, False)
    #GPIO.output(in2_pin, True)

def fancontrol(pwm): #assume fan is powered by GPIO
    #if pwm>0:
    #    p.start(pwm)
    #elif pwm == 0:
    #    GPIO.output(fan_pin, False)
 
def pumpcontrol(pwm):
    if pwm>0:
        #p.start(pwm)
        clockwise()
    if pwm == 0:
        #p.stop()



                    
tempcon = Controller()
desired_temp=25

while True:
    #Pd Controller
    temp_current=read_temp()
    error=(desired_temp-temp_current)
    diff_err=(temp_current-temp_prv)/0.4 # 0.2sec delay everytime pass by read_temp()
    
    temp_prv=read_temp()
    temp=[temp_prv,error,diff_err]    
    instr = tempcon.step(temp)
    print temp_prv,instr
    #fancontrol(instr[0])
    pumpcontrol(instr[1])