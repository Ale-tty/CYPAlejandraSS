NUM = int (input ( "Escribe el tipo de opcion de calculo (1 = 100 *v), (2= 100 ** v), (3 = 100/v) (Otro numero = 0) ")) 
V = int (input ("Escribe el numero al que le deseas hacer el calculo "))
if NUM == 1: 
    VAL= 100 * V 
    print (f" El resultado es {VAL}")
if NUM == 2:
    VAL = 100 ** V
    print (f"El resultado es {VAL}")
if NUM == 3:
    VAL = 100 / V
    print (f"El resultado es {VAL}")
if NUM > 3: 
    VAL = 0 
    print (f"El resultado es {VAL}")
print ("Fin del programa")
