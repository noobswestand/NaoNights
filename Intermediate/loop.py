import time,random
from naoqi import ALProxy
ip="127.0.0.1"
port=49267
touch=ALProxy("ALTouch",ip,port)
tts=ALProxy("ALTextToSpeech",ip,port)


tts.say("Could you touch my head?")

while True:
    t=touch.getStatus()
    if t[0][1]==True:
        break

tts.say("Good job!")







'''
run=True
touches=[["Head","Head"],
         ["LHand","Left Hand"],
         ["RHand","Right Hand"],
         ["LFoot/Bumper/Left","Left Foot"],
         ["RFoot/Bumper/Left","Right Foot"]]
touch_requested=-1


while run:
    t=touch.getStatus()

    if touch_requested==-1:#set which touch we should check for
        touch_requested=int(random.random()*len(touches))
        tts.say("Could you touch my "+touches[touch_requested][1])
        print touches[touch_requested][0]
    else:#Checking the touch
        for item in t:
            if item[0]==touches[touch_requested][0]:
                
                break
        
        
    time.sleep(0.5)
'''
