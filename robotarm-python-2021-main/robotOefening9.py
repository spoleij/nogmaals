from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
robotArm.speed = 4                 # < max 12 lines of code, maar dit is als test anders is het zo langzaam. verwijder line
for x in range (4):
    for x in range (4):
        robotArm.grab()
        [robotArm.moveRight() for movement in range (5)]            # heb de for / range code korter kunnen schrijven!!!!
        robotArm.drop()                                             # met [ ] , dus de moveright() zit nu in dezelfde line.
        [robotArm.moveLeft() for movement in range (4)]
    [robotArm.moveLeft() for x in range (4)]    
robotArm.wait()