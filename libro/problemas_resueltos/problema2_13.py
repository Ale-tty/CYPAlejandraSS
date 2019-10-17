MAT =int (input ("Introduce tu matricula "))
CARR = str (input ("Introduce tu carrera ")) 
SEM = int (input ("Inroduce tu semestre "))
PROM = float (input ("Introduce tu promedio "))
if CARR == "economia": 
    if SEM >= 6:
        if PROM >= 8.8:
            print (f"{MAT} de la carrera {CARR} estas aceptado")
    else: 
        print ("No seleccionado")
elif CARR == "computacion": 
    if SEM > 6:
        if PROM > 8.5:
            print (f"{MAT} de la carrera {CARR} estas aceptado")
    else: 
        print ("No seleccionado") 
<<<<<<< HEAD
elif CARR == "contabilidad": 
    if SEM > 5:
        if PROM > 8.5:
            print (f"{MAT} de la carrera {CARR} estas aceptado") 
=======
else CARR == contabilidad : 
    if (SEM > 5) (PROM > 8.5):
        print (f"{MAT} de la carrera {CARR} estas aceptado") 
>>>>>>> 1934788e2cb96195a6a958cc5f7b20bd8e422bff
    else: 
        print ("No seleccionado") 
elif CARR == "administracion":
    if SEM > 5:
        if PROM > 8.5:
            print (f"{MAT} de la carrera {CARR} estas aceptado")
    else:
        print ("No seleccionado")
print ("Fin del programa") 
