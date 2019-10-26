SUMOTR = 0
SUMPOS = 0
CUEPOS = 0
N = int (input("Introduce un numero entero "))
for I in range(0,N,1):
    NUM = int (input("Introduce otro numero"))
    if NUM > 0:
        SUMPOS+= NUM
        CUEPOS+= 1
        I+= 1
    else:
        SUMOTR+= NUM
        I+= 1
else:
    PROGEN = (SUMPOS + SUMOTR) / N
    PROPOS = SUMPOS / CUEPOS
    print (f"La cantidad de numeros positivos son {CUEPOS}, el promedio de numeros positivos son {PROPOS} y el promedio general de los numeros son {PROGEN}")
print ("Fin del programa")        
            
