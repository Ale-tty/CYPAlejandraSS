CATE = int (input ("Escoge la categoria de empleado (1 = SUE * 1.15), (2 = SUE *1.10), (3 = SUE * 1.08), (4 = SUE * 1.07) "))
SUE = float (input ("Dime cual es tu sueldo "))
if CATE == 1: 
    NSUE = SUE * 1.15 
    print (f"Su nuevo sueldo es de ${NSUE}")
if CATE == 2: 
    NSUE = SUE * 1.10 
    print (f"Su nuevo sueldo es de ${NSUE}")
if CATE == 3: 
    NSUE = SUE * 1.08 
    print (f"Su nuevo sueldo es de ${NSUE}")
if CATE == 4: 
    NSUE = SUE * 1.07 
    print (f"Su nuevo sueldo es de ${NSUE}") 
print ("Fin del programa") 
