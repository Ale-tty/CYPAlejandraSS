MAT =int (input ("Introduce tu matricula "))
CARR = str (input ("Introduce tu carrera ")) 
SEM = int (input ("Inroduce tu semestre "))
PROM = float (input ("Introduce tu promedio "))
if CARR == economia : 
    if (SEM >= 6) (PROM >= 8.8):
        print (f"{MAT} de la carrera {CARR} estas aceptado")
    else: 
        print ("No seleccionado")
elif CARR == computacion : 
    if (SEM > 6) (PROM > 8.5): 
        print (f"{MAT} de la carrera {CARR} estas aceptado")
    else: 
        print ("No seleccionado") 
elif CARR == contabilidad : 
    if (SEM > 5) (PROM > 8.5):
        print (f"{MAT} de la carrera {CARR} estas aceptado") 
    else: 
        print ("No seleccionado") 
print ("Fin del programa") 
