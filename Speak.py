#!/usr/bin/python

# SOFTENG 206 Assignment 3
# Andrew Luey and Arunim Talwar
# Date: September 2011
# Description: Festival functions


from os import killpg, setsid, getpgid
from subprocess import Popen, PIPE
from signal import signal, SIGKILL


class Festival:

    def __init__(self):
        """ Start the speaking functionality """
        self.proc = Popen(["festival", "--pipe"], stdin=PIPE, preexec_fn=setsid)
        self.proc.stdin.write("(audio_mode 'async)\n")

    def speakSelected(self, text):
        """ Speaks the string input """
        self.proc.stdin.write('(SayText "%s")\n' % text)

    def restartFest(self):
        """ Stops the current speech """
        killpg(getpgid(self.proc.pid), SIGKILL)
        self.proc = Popen(["festival", "--pipe"], stdin=PIPE, preexec_fn=setsid)
        print "temporary test message: speaking stopped"
