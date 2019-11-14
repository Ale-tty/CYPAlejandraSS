PRI = 0
SEG = 1
I = 3
for I in range(3,181,1):
    SIG = PRI + SEG
    PRI = SEG
    SEG = SIG
    I+= 1
else:
    print (f"El numero de la serie es {SIG}")
    
