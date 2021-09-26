from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
robotArm.speed = 3               # < max 15 lines of code, maar dit is als test anders is het zo langzaam. verwijder line
moveR = 9
moveL = 8
for movement in range (5):
    robotArm.grab()
    [robotArm.moveRight() for movement in range (moveR)]
    robotArm.drop() 
    [robotArm.moveLeft() for movement in range (moveL)]
    moveR = moveR -2
    moveL = moveL -2
robotArm.wait()

