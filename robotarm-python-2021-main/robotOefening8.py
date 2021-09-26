from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
robotArm.speed = 3                 # < max 11 lines of code, maar dit is als test anders is het zo langzaam. verwijder line
robotArm.moveRight()
for total in range (7):
    for movement in range (8):
            robotArm.grab()
            robotArm.moveRight()
    robotArm.drop()
    for movement in range (8):
        robotArm.moveLeft()
robotArm.wait()