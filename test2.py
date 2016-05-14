# Krystal Kwan
# 2/7/2016
# Flash an LED light
#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

GPIO.output(23, True)
GPIO.output(24, True)
GPIO.output(25, True)
GPIO.output(12, True)
GPIO.output(16, True)
GPIO.output(20, True)
GPIO.output(4, True)
GPIO.output(17, True)
