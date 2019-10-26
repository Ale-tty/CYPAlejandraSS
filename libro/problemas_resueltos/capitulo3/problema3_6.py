MAY = -100000
MEN = 100000
N = int (input("Introduce el numero de veces que deseas repetir el programa"))
I = 1
for I in range(0,N,1):
    NUM = int (input("Introduce un numero entero"))
    if NUM > MAY:
        MAY = NUM
    if NUM < MEN:
        MEN = NUM
    I+= 1
else:
    print (f"Es el numero mayor {MAY} y el numero menor es {MEN}")
