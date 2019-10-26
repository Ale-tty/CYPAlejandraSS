SUMPAR = 0
SUMIMP = 0
CUEPAR = 0
i = 1 
for i in range(1,11,1):
    NUM = int(input("Introduce un numero"))
    if NUM != 0:
        if ((-1) ** NUM)>0:
            SUMPAR+= NUM 
            CUEPAR+= 1 
            i+= 1
        else: 
            SUMIMP+= NUM 
            i+= 1
PROPAR = SUMPAR / CUEPAR 
print (f"El promedio de numeros pares {PROPAR} y la suma de los numeros impares es {SUMIMP}")
