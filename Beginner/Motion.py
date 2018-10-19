
from naoqi import ALProxy
ip="127.0.0.1"
port=63789
motionProxy = ALProxy("ALMotion", ip, port)


names=["HeadYaw","HeadPitch"]

angles=[0.2,-0.2]


fractionMaxpeed=0.2
motionProxy.setAngles(names,angles,fractionMaxpeed)


