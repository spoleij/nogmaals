# Herhaal een input() tot het resultaat daarvan gelijk is aan ‘quit’ Print het aantal iteraties per iteratie.
text = input ('enter command: ')
fout = 0
while text != 'quit':
    fout = fout +1
    print ("iteraties: " + str(fout))
    text = input ('enter command: ')