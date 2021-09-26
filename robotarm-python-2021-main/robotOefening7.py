from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
robotArm.speed = 3                 # < max 11 lines of code, maar dit is als test anders is het zo langzaam. verwijder line
for stacks in range (5):
    robotArm.moveRight()
    for movement in range (6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    robotArm.moveRight()
robotArm.wait()