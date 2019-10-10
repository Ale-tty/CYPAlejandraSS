MAT = int (input("Introduce tu matricula "))
CAL1 = float (input("Introduce tu primer calificacion "))
CAL2 = float (input("Introduce tu segunda calificacion "))
CAL3 = float (input("Introduce tu tercera calificacion "))
CAL4 = float (input("Introduce tu cuarta calificacion "))
CAL5 = float (input("Introduce tu quinta calificacion "))
PRO = (CAL1+CAL2+CAL3+CAL4+CAL5) / 5 
if PRO >= 6: 
    print (f"{MAT} este es tu promedio {PRO}, estas aprobado")
else: 
    print (f"{MAT} este es tu promedio {PRO}, estas reprobado")
print ("Fin del programa")
