from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

# Jouw python instructies zet je vanaf hier:
blocks = 9
robotArm.grab()
for movement in range (blocks):
    robotArm.moveRight()
robotArm.drop()

blocks = 5
for moveblock in range (blocks):
    robotArm.moveLeft()
robotArm.grab()

blocks = 5
for moveblock in range (blocks):
    robotArm.moveRight()
robotArm.drop()

blocks = 2
for moveblock in range (blocks):
    robotArm.moveLeft()
robotArm.grab()

blocks = 2
for moveblock in range (blocks):
    robotArm.moveRight()
robotArm.drop()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()