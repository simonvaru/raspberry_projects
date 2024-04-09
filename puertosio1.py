import RPi.GPIO as GPIO
import time

#pin definitons
powPin=18
ledPin=23
butPin=17

duty=75

#setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(powPin, GPIO.OUT)
GPIO.setup(powPin, GPIO.OUT)
GPIO.setup(powPin, GPIO.IN)
