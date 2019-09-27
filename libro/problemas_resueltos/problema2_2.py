P = int (input ("Introduce un numero entero "))
Q = int (input ("Introduce un numero entero "))
EXP = P ** 3 + Q ** 4 - 2 * P ** 2 
if EXP < 680:
    print (f"Los numeros {P} y {Q} son menores que 680") 
else:
    print ("Los numeros son mayores que 680")
print ("Fin del programa")
