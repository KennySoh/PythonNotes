print"\n Qns 1\n"
def celsius_to_fahrenheit(C):
    F=C*9/5.0+32.0
    return F
print celsius_to_fahrenheit (0)
print celsius_to_fahrenheit (-40)
print celsius_to_fahrenheit (100) 

print"\n Qns 2\n"
from math import pi
def vol_cylinder(radius,length):
    area=radius*radius*pi
    vol=area*length
    return area,vol
print vol_cylinder (1.0 ,2.0)
print vol_cylinder (2.0 ,2.3)
print vol_cylinder (1.5 ,4)
print vol_cylinder (2.2 ,5.0)

print"\n Qns 3\n"
def wind_chill_temp(ta, v):
    twc="Does not satisfy constraints"
    if ta<41 and ta>-58 and v>=2:
        twc=35.74+0.6215*ta-35.75*v**0.16+0.4275*ta*v**0.16
    return twc
print wind_chill_temp(5.3 ,6)
print wind_chill_temp(2.2 ,4)

ta_1=input("Outside temperature in Fahrenheit: ")
v_1=input("Wind speed in miles per hour: ")
print ("\nwind chill index: " + str(wind_chill_temp(ta_1, v_1)))

print"\n Qns 4\n"
def bmi(weight,height):
    weight = weight*0.45359237#weight to pounds
    height = height*0.0254#height to meter
    bmi=weight / height**2
    return bmi
print bmi (120 ,60)
print bmi (100 ,50)
print bmi (200 ,80)
print bmi (95.5 ,50)

weight_1=input("Weight in pounds: ")
height_1=input("Height in inches:")
print ("\nBMI: " + str(bmi(weight_1,height_1)))

print"\n Qns 5\n"
def investment_val(amount, annualRate, years):
    monthlyRate=annualRate/12.0/100
    months=years*12.0
    FIV=amount*(1.0+monthlyRate)**months
    FIV=round(FIV,2)
    return FIV

print investment_val (1000 ,4.25 ,1)
print investment_val (1500 ,3.25 ,2)
print investment_val (1000 ,2.25 ,0.5)
print investment_val (2000 ,4.25 ,3)

amount_1=input("Enter investment amount: ")
annualRate_1=input("Enter annual interest rate (%): ")
years_1=input("Enter number of years: ")

print ("\nAccumulated value is " + str(investment_val(amount_1, annualRate_1, years_1)))


