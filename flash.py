# Krystal Kwan
# 12/23/2015
# Flash an LED light
#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from time import sleep
import pifacedigitalio

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def flash():
  GPIO.output(24, True)
  GPIO.output(25, True)
  GPIO.output(12, True)
  GPIO.output(16, True)
  GPIO.output(20, True)
  GPIO.output(4, True)
  time.sleep(0.5)
  GPIO.output(24, False)
  GPIO.output(25, False)
  GPIO.output(12, False)
  GPIO.output(16, False)
  GPIO.output(20, False)
  GPIO.output(4, False)
  time.sleep(0.5)

while True:
  if (GPIO.input(21) ==0):
    for i in range(20):
      flash()
  if (GPIO.input(18) ==0):
    for j in range(
