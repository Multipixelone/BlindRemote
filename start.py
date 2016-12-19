## Just FYI, this probably COULD be coded cleaner... If you think you could help, feel free to submit a pull request!
## Import Files
print('eyeRemote by Multipixelone on Github.')
from TakePicture import TakePicture
import picamera
from LocalVariables import takepicture
print('Imported Picture Taking')
import Cloudsight
from Cloudsight import UploadPicture
import cloudsight
import requests
print('Imported Image Uploading')
import RPi.GPIO as GPIO
print('Imported GPIO')
from PlaySounds import Welcome
from PlaySounds import ErrorNetwork
from PlaySounds import SpeakWord
print('Imported Sound Playing')
from time import sleep
print('Imported Sleeping')
#file = "Tests/Tests.txt"
#path = os.getcwd()+file 

## Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(takepicture, GPIO.IN, pull_up_down=GPIO.PUD_UP)

## Functions Available:
#TakePicture()
#UploadPicture()
#ErrorNetwork()
#Welcome()
#SpeakWord(WORD)

## Code to upload image.jpg, return a json response, import that, and then speak it out
#UploadPicture()
#from CloudsightAPI import item
#SpeakWord(item)

## Code to take picture:
#print('Waiting for inputs!')
#while True:
#  if (GPIO.input(takepicture)):
#    TakePicture()



## Actual code now: 
Welcome()
SpeakWord("Ready to test!")
print('Waiting for inputs!')
while True:
  input_state = GPIO.input(takepicture)
  if input_state == False:
    SpeakWord("Taking Picture")
    TakePicture()
    SpeakWord("Ready for data")
    try:
        file = open("Tests/Tests", 'a+')
        number = raw_input('What is the number of the object you are scanning? [1-...] ')
        name = raw_input('What is the object you are scanning? [NAME] ')
        distance = raw_input('What is the relative distance? [CENTIMETER] ')
	UploadPicture()
    except requests.ConnectionError: ## Might need to be changed after the program shift
        ErrorNetwork()
    else:
        from Cloudsight import item
	file.write("\n")
        file.write(number + "\n")
        file.write(name + "\n")
        file.write(distance + "\n")
        file.write(item + "\n")                    
        file.close()
        SpeakWord(item)

    
