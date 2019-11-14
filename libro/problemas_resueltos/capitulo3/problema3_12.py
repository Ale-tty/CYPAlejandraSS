MASUE = 0
I = 1
N = int(input("Introduce el numero de empleados"))
for I in range(0,N,1):
    NUMEMP = int(input("Que empleado eres"))
    SUE = float(input("Mete tu sueldo "))
    if SUE > MASUE:
        MASUE = SUE
        MANUM = NUMEMP
        I+= 1
    else:
        I+= 1
else:
    print (f"El empleado que gana mas es {MANUM} y su sueldo es ${MASUE}")
print ("Fin del programa") 
