#!/usr/bin/python

# SOFTENG 206 Assignment 3
# Andrew Luey and Arunim Talwar
# Date: September 2011
# Description: Festival functions


from os import killpg, setsid, getpgid
from subprocess import Popen, PIPE
from signal import signal, SIGKILL


def speak(text):
    """ Speaks the string input """
    proc.stdin.write('(SayText "%s")\n' % text)

def restartFest():
    """ Stops the current speech """
    global proc
    killpg(getpgid(proc.pid), SIGKILL)
    proc = Popen(["festival", "--pipe"], stdin=PIPE, preexec_fn=setsid)
    
# Start the speaking functionality
proc = Popen(["festival", "--pipe"], stdin=PIPE, preexec_fn=setsid)
proc.stdin.write("(audio_mode 'async)\n")
