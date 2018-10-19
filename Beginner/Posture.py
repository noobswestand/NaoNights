
from naoqi import ALProxy
ip="127.0.0.1"
port=52543
postureProxy = ALProxy("ALRobotPosture", ip, port)
postureProxy.goToPosture("Sit", 1.0)
