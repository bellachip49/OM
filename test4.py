#!/usr/bin/env python
# Krystal Kwan
# 12/23/2015
# Flash an LED light

import RPi.GPIO as GPIO
import subprocess
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
  if (GPIO.input(19) == 1):
      print "Play music"
      sleep(3)



