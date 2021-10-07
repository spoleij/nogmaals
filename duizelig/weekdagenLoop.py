# OPDRACHT:
# Vraag een dag van de week op (ma,di,wo,do,vr,za,zo) Print alle dagen tot aan de opgegeven dag

welkeDag = input ("Geef een dag van de week: ")
alleDagen = ['maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag']
maakIndex = alleDagen.index(welkeDag)
sliceIndex = alleDagen[:maakIndex+1]                # +1 anders print het programma niet de dag van de welkeDag input
while welkeDag in alleDagen:
    print (*sliceIndex)
    break
     
