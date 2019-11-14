AP1 = 0
AP2 = 0
AP3 = 0
AP4 = 0
AP5 = 0
RECAU= 0
P1 = float(input("Introduce el precio de la localidad 1 "))
P2 = float(input("Introduce el precio de la localidad 2 "))
P3 = float(input("Introduce el precio de la localidad 3 "))
P4 = float(input("Introduce el precio de la localidad 4 "))
P5 = float(input("Introduce el precio de la localidad 5 "))
CLAVE = int(input("Mete el tipo de localidad"))
CANT = int(input("Introduce la cantidad de boletos vendidos"))
while CLAVE != -1:
    while CANT != -1:
        if CLAVE == 1:
            PRE = P1 * CANT
            AP1 = AP1 + CANT
        elif CLAVE ==2:
            PRE = P2 * CANT
            AP2 = AP2 + CANT
        elif CLAVE == 3:
            PRE = P3 * CANT
            AP3 = AP3 + CANT
        elif CLAVE == 4:
            PRE = P4 * CANT
            AP4 = AP4 + CANT
        elif CLAVE == 5:
            PRE = P5 * CANT
            AP5 = AP5 + CANT
        print (f"La localidad es {CLAVE}, la cantidad de boletos vendidos es de {CANT} y el total vendido fue de {PRE}")
        RECAU+= PRE
        CLAVE = int(input("Introduce la localidad "))
        CANT = int(input("Introduce la cantidad de boletos vendidos "))
else:
    print (f"La cantidad de boletos tipo 1 es de {AP1}")
    print (f"La cantidad de boletos tipo 2 es de {AP2}")
    print (f"La cantidad de boletos tipo 3 es de {AP3}")
    print (f"La cantidad de boletos tipo 4 es de {AP4}")
    print (f"La cantidad de boletos tipo 5 es de {AP5}")
    print (f"La recaudacion del estado es de {RECAU}")
print ("Fin del programa")
