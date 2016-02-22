#!/usr/bin/env python

import subprocess

print subprocess.Popen("su - pi -c '/usr/bin/mpg321 /home/pi/Documents/audio_sandbox/proofyourlove.mp3'", shell=True, stdout=subprocess.PIPE).stdout.read()

