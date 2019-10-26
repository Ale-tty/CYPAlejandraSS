NOM = 0
SUE = float (input("Introduce tu sueldo"))
while SUE != -1 :
    if SUE < 1000:
        NSUE= SUE*1.15
        NOM+=NSUE
    else:
        NSUE = SUE *1.12
        NOM+=NSUE
    print (f"El nuevo sueldo es de {NSUE}")
    SUE = float (input("Dame otro sueldo"))
else:
    print (f"La nomina es de {NOM}")
