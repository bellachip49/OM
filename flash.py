# Krystal Kwan
# 12/23/2015
# Flash an LED light
#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
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
    for j in range(10):
      for k in range(1):
        GPIO.output(24, True)
        time.sleep(0.02)
        GPIO.output(24, False)
        time.sleep(0.02)
        GPIO.output(25, True)
        time.sleep(0.02)
        GPIO.output(25, False)
        time.sleep(0.02)
        GPIO.output(12, True)
        time.sleep(0.02)
        GPIO.output(12, False)
        time.sleep(0.02)
        GPIO.output(16, True)
        time.sleep(0.02)
        GPIO.output(16, False)
        time.sleep(0.02)
        GPIO.output(4, True)
        time.sleep(0.02)
        GPIO.output(4, False)
        time.sleep(0.02)
      for x in range(7):
        GPIO.output(4, True)
        time.sleep(0.02)
        GPIO.output(4, False)
        time.sleep(0.02)
        GPIO.output(16, True)
        time.sleep(0.02)
        GPIO.output(16, False)
        time.sleep(0.02)
        GPIO.output(12, True)
        time.sleep(0.02)
        GPIO.output(12, False)
        time.sleep(0.02)
        GPIO.output(25, True)
        time.sleep(0.02)
        GPIO.output(25, False)
        time.sleep(0.02)
        GPIO.output(24, True)
        time.sleep(0.02)
        GPIO.output(24, False)
        time.sleep(0.02)
