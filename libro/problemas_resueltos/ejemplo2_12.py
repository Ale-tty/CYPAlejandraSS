A = int (input ("Escribe un numero entero "))
B = int (input ("Escribe un numero entero "))
C = int (input ("Escribe un numero entero ")) 
if A > B: 
    if A > C: 
        if B > C: 
            print (f"Los numeros de forma descendente quedan asi {A},{B},{C}") 
        else: 
            print (f"Los numeros de forma descendente quedan asi {A},{C},{B}") 
    else: 
        print (f"Los numeros de forma descendente quedan asi {C},{A},{B}") 
else: 
    if B > C: 
        if A > C: 
            print (f"Los numeros de forma descendente quedan asi {B},{A},{C}") 
        else: 
            print (f"Los numeros de forma descendente quedan asi {B},{C},{A}") 
    else:
        print (f"Los numeros de forma descendente quedan asi {C},{B},{A}") 
print ("Fin del programa") 
