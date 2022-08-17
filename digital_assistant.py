from turtle import listen
import minionVPA
import imp
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import requests
import json


time.sleep(2)
minionVPA.respond("Hi Dante, what can I do for you?")
listening = True
while listening == True:
    data = listen()
    listening = minionVPA.digital_assistant(data)
