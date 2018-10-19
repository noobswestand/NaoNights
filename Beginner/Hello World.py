
from naoqi import ALProxy

ip="127.0.0.1"
port=52543
tts = ALProxy("ALTextToSpeech", ip, port)
tts.setParameter("speed", 200)
tts.setParameter("pitchShift", 1.5)
tts.say("Hello World!")

