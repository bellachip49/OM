#!/usr/bin/env python
# Krystal Kwan
# 12/23/2015
# Flash an LED light

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
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.output(23, False)
GPIO.output(24, False)
GPIO.output(25, False)
GPIO.output(12, False)
GPIO.output(16, False)
GPIO.output(20, False)
GPIO.output(4, False)
GPIO.output(17, False)

def flash():
  print "blink"
  GPIO.output(23, True)
  GPIO.output(24, True)
  GPIO.output(25, True)
  GPIO.output(12, True)
  GPIO.output(16, True)
  GPIO.output(20, True)
  GPIO.output(4, True)
  GPIO.output(17, True)
  sleep(0.5)
  GPIO.output(23, False)
  GPIO.output(24, False)
  GPIO.output(25, False)
  GPIO.output(12, False)
  GPIO.output(16, False)
  GPIO.output(20, False)
  GPIO.output(4, False)
  GPIO.output(17, False)
  sleep(0.5)

while True:
  if (GPIO.input(18) ==0):
      for j in range(10):
        for k in range(1):
          GPIO.output(23, True)
          sleep(0.02)
          GPIO.output(23, False)
          sleep(0.02)
          GPIO.output(24, True)
          sleep(0.02)
          GPIO.output(24, False)
          sleep(0.02)
          GPIO.output(25, True)
          sleep(0.02)
          GPIO.output(25, False)
          sleep(0.02)
          GPIO.output(12, True)
          sleep(0.02)
          GPIO.output(12, False)
          sleep(0.02)
          GPIO.output(20, True)
          sleep(0.02)
          GPIO.output(20, False)
          sleep(0.02)
          GPIO.output(16, True)
          sleep(0.02)
          GPIO.output(16, False)
          sleep(0.02)
          GPIO.output(4, True)
          sleep(0.02)
          GPIO.output(4, False)
          sleep(0.02)
          GPIO.output(17, True)
          sleep(0.02)
          GPIO.output(17, False)
          sleep(0.02)
          print "circled"
  if (GPIO.input(21) ==0):
    for i in range(10):
      flash()
