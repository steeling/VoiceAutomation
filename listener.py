#!/usr/bin/python
import speech_recognition as sr
import time

class Listener():
  def __init__(self):
    print "Starting up"

  def listen(self):
    while(True):
      r = sr.Recognizer()  
      print "Listening"
      with sr.Microphone() as source:                # use the default microphone as the audio source
        # r.adjust_for_ambient_noise(source)         # listen for 1 second to calibrate the energy threshold for ambient noise levels

        audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

      try:
        print(r.recognize(audio))                  # recognize speech using Google Speech Recognition
      except LookupError:                            # speech is unintelligible
        print("Could not understand audio")

  # def callback(self, recognizer, audio):                          # this is called from the background thread
  #   try:
  #     print "Looking up: "
  #     print(recognizer.recognize(audio))  # received audio data, now need to recognize it
  #   except LookupError:
  #     print("Oops! Didn't catch that")
  #   finally:
  #     print "stopping"

  # def listen2(self):
  #   r = sr.Recognizer()
  #   m = sr.Microphone()
  #   with m as source: r.adjust_for_ambient_noise(source)      # we only need to calibrate once, before we start listening
  #   self.stop_listening = r.listen_in_background(m, self.callback)

def activate_listner():
  try:
    l = Listener()
    l.listen()
    while(True):
      time.sleep(1)
  except:
    activate_listner()

def main():
  activate_listner()


if __name__ == "__main__":
  main()

# try:
#     list = r.recognize(audio,True)                  # generate a list of possible transcriptions
#     print("Possible transcriptions:")
#     for prediction in list:
#         print(" " + prediction["text"] + " (" + str(prediction["confidence"]*100) + "%)")