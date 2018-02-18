from firebase import firebase
from eBot import eBot
from time import sleep

url = "https://d-digitalworld.firebaseio.com/" # URL to Firebase database
token = "yGQ8IFQZ2noOvltPrcnHBzc71NbIdw4m8Dcj6tNi" # unique token used for authentication

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = firebase.FirebaseApplication(url, token)

#print "Reading from my database."
#print firebase.get('/age') # get the value from the node age

#firebase.put('/','pie',3.14)

ebot_firebase=firebase.get('/move')
print ebot_firebase



def forward(speed_left,speed_right, duration):
    # Write your code here
    ebot.wheels(speed_left, speed_right) # make the robot move at 100% speed on both wheels
    sleep(duration) # wait for 5 seconds

ebot = eBot.eBot() # create an eBot object
ebot.connect() # connect to the eBot via Bluetooth

for move in ebot_firebase:
    if move==u'left':
        forward(-1,1,0.555)
    elif move==u'right':
        forward(1,-1,0.555)
    elif move==u'forward':
        forward(1,1,0.555)
    else:
        forward(0,0,0)
ebot.disconnect()
