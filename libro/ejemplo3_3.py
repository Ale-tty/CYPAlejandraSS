CUERCER = 0 
N = int(input("Dame un numero entero positivo "))
for I in range(0,N,1): 
    NUM = int(input("Ingresa un entero ")) 
    if NUM == 0: 
        CUERCER += 1 
print (f"El numero de 0's capturados fue: {CUERCER}")
