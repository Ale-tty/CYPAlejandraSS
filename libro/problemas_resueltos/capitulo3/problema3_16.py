TIPO1 = 0
TIPO2 = 0
TIPO3 = 0
TIPO4 = 0
TIPO5 = 0
MCTIPO2 = 0
N = int (input("Introduce los años "))
I = 1
for I in range(1,N+1,1):
    J = 1
    TOTVIN = 0
    for J in range(1,6,1):
        V = float (input("La cantidad de litros"))
        TOTVIN+= V
        if J == 1:
            TIPO1+= V
            J+= 1
        elif J == 2:
            TIPO2+= V
            J+= 1
            if V > MICTIPO2:
                MICTIPO2 = V
                AÑO = I
                J+= 1
            else:
                J+= 1
        elif J == 3:
            if V == 0:
                print (f"El año {I} no se produjo vino del tipo 3")
                J+= 1
        elif J == 4:
            TIPO4+= V
            J+= 1
        elif J == 5:
            TIPO5+= V
            J+= 1
    else:
        print (f"El total de litrod producidos es de {TOTVIN}")
        I+= 1
else:
    print (f"Total de vino del tipo 1 es de {TIPO1}")
    print (f"Total de vino del tipo 2 es de {TIPO2}")
    print (f"Total de vino del tipo 3 es de {TIPO3}")
    print (f"Total de vino del tipo 4 es de {TIPO4}")
    print (f"Total de vino del tipo 5 es de {TIPO5}")
    print (f"Año en que se produjo mayor cantidad vino tipo2 es {AÑO} y los litros {MCTIPO2}")
        
    
