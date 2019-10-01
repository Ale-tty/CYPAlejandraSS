SUE = float ( input ("Cual es tu salario? "))
if SUE < 1000: 
    NSUE = SUE * 1.15
    print (f"Este es tu nuevo sueldo {NSUE}")
else: 
    NSUE = SUE * 1.12
    print (f"Este es tu nuevo sueldo {NSUE}")
print ("Fin del programa")
