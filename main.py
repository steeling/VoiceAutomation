#!/usr/bin/python
import subprocess

class VoiceAutomation:
  def __init__(self):
    print "init"

  def spawn_listener(self, listener=["listener.py"], receiver=["receiver.py"]):
    self.listener = subprocess.Popen(listener, bufsize=1, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    self.receiver = subprocess.Popen(receiver, bufsize=1, stdin=self.listener.stdout, stdout=subprocess.PIPE)
    self.listener.stdout.close()