# OPDRACHT:
# Vraag een dag van de week op (ma,di,wo,do,vr,za,zo) Print alle dagen tot aan de opgegeven dag

welkeDag = input ("Geef een dag van de week: ")
alleDagen = ['maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag']
while welkeDag in alleDagen:
    print (alleDagen[:welkeDag])
    break
     
    
# alleDagen = int(alleDagen)
# y = list(map(int, alleDagen))
# , sep = "\n"