A = float (input ("Introduce un numero "))
B = float (input ("Introduce un numero "))
C = float (input ("Introduce un numero "))
DIS = (B ** 2) - (4 * A* C) 
if DIS >= 0 :
    X1 = ((-B) + (DIS ** 0.5)) / (2 * A)
    X2 = ((-B) - (DIS ** 0.5)) / (2 * A )
    print (f"Las raices reales son: X1 = {X1} Y X2 = {X2}")
else: 
    print ("No tiene raices") 
print ("Fin del programa")
