MED = 0
CHI = 0
GRA = 0
I = 1
N= int(input("Introduce el numero de ventas "))
for I in range(0,N,1):
    V = float(input("De cuanto fue la venta? "))
    if V <= 200:
        CHI+= 1
        I+= 1
    else:
        if V < 400:
            MED+= 1
            I+= 1
        else:
            GRA+= 1
            I+= 1
else:
    print (f"El numero de ventas menores de $200 es de {CHI}, el numero de ventas de $200 a $400 es de {MED} y el numero de ventas mayores a $400 es de {GRA}")
print ("Fin del programa")
