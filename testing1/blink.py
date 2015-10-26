#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

# Create a function to blink

def blink(pin):
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(.125)
	GPIO.output(pin,GPIO.LOW)
	time.sleep(.125)
	return

# use R Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# Setup output channel

GPIO.setup(11, GPIO.OUT)

# Blink pin 17 x 50
for i in range (0,50):
	blink(11)
