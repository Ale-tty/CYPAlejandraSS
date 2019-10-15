CLAVE = int (input ("Introduce la clave de la zona que marcaste ")) 
NUMIN = int (input ("Introduce durante cuantos minutos hablaste "))
COST = 0 
if CLAVE == 12 :
    COST = NUMIN *2 
elif CLAVE == 15: 
    COST = NUMIN * 2.2 
elif CLAVE == 18 :
    COST = NUMIN * 4.5 
elif CLAVE == 19: 
    COST = NUMIN * 3.5 
elif CLAVE == 23 : 
    COST = NUMIN * 6
elif CLAVE == 25: 
    COST = NUMIN * 6
elif CLAVE == 29: 
    COST = NUMIN * 5 
print (f"El costo total de la llamada es ${COST}")
