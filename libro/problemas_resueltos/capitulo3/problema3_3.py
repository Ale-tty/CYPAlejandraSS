SERIE = 0
N = int (input("Introduce un numero entero "))
BAND = "T"
I = 1
for I in range(1,N,1):
    if BAND == "T":
        SERIE= SERIE+1 /I
        BAND = "F"
        I+=1
        print (SERIE)
    else:
        SERIE = SERIE-1 /I
        BAND = "T"
        I+=1
        print (SERIE)
else:
    print (f"El resultado de la serie es {SERIE}")
