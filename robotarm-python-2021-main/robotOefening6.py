from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:

blocks = 9
for movement in range (blocks):
    robotArm.moveRight()
times = 8
blocks = 2
for blocktimes in range(times):
    for movement in range (blocks):
        robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()