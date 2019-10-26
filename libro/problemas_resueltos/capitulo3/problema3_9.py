SERIE = 0
N = int (input("Introduce el numero de la serie "))
I = 1
for I in range(1,N+1,1):
    SERIE = SERIE + I ** I
    I+= 1
else:
    print (f"La serie es {SERIE}")
print("Fin del programa")
