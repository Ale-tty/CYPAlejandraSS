CL = 0
CUENTA = 0
TIPO = str (input("Introduce tu tipo de llamada, I si es internacional, N si es nacional y L si es local"))
DUR = int (input("Introduce la duracion de la llamada"))
while TIPO!= "x":
    while DUR != -1:
        if TIPO == "I":
            if DUR > 3:
                COSTO = 7.59 + (DUR - 3) * 3.03
                print (COSTO)
            else:
                COSTO = 7.59
                print(COSTO)
        elif TIPO == "L":
            CL+= 1
            print(COSTO)
            if CL > 50:
                COSTO = 0.60
                print (COSTO)
            else:
                COSTO = 0
                print (COSTO)
        elif TIPO == "N":
            if DUR > 3:
                COSTO = 1.20 + (DUR - 3) * 0.48
                print (COSTO)
            else:
                COSTO = 120
                print (COSTO)
        CUENTA+= COSTO 
        TIPO = str (input("Introduce tu tipo de llamada, I si es internacional, N si es nacional y L si es local"))
        DUR = int (input("Introduce la duracion de la llamada"))
else:
    print(f"El costo de las llamadas fue de {CUENTA}")
    
                
    
