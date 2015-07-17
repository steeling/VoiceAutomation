#!/usr/bin/python
import subprocess

class VoiceAutomation:
	def __init__(self):
		print "init"

	def spawn_listener(self, listener=["listener.py"]):
		self.listener = subprocess.Popen(listener, bufsize=1, stdout=subprocess.PIPE)

	
