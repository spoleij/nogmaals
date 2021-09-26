from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.speed = 3
robotArm.randomLevel(1,7)
for movement in range (9):
    robotArm.grab()
    color = robotArm.scan()
    if color in ['white','red','green','blue','yellow']:                #dit checkt of de arm uberhaupt een blok vast heeft
        [robotArm.moveRight() for movement in range (9)]                #kleuren uit RobotArm.py gehaald
        robotArm.drop()
        [robotArm.moveLeft() for movement in range (9)]
    else:                                                               #zo niet: de arm stopt
        robotArm.wait()

robotArm.wait()