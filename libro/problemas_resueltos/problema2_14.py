TIPOENF = int(input("Cual es tu enfermedad? "))
EDAD = int(input("Cual es su edad? "))
DIAS = int(input("Cuantos dias estuvo hospitalizado? "))
COSTOT = 0
if TIPOENF == 1: 
    COSTOT = DIAS * 25 
elif TIPOENF == 2: 
    COSTOT = DIAS * 16
elif TIPOENF ==3:
    COSTOT = DIAS *20
elif TIPOENF == 4:
    COSTOT = DIAS * 32 
if EDAD >= 14:
    if EDAD <= 22: 
        COSTOT = COSTOT * 1.10 
print (f"El costo total es de {COSTOT}")
