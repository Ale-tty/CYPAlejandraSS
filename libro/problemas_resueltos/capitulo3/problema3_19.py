N = int(input("Introduce el limite de los numeros naturales"))
I = 1
for I in range(1,N,1):
    SUM = 0
    J = 1
   
    for J in range(1,int(I/2),1):
        if (I % J) == 0:
            SUM+= J
            J+= 1
        else:
            J+= 1
    else:
        if SUM == 1:
            print(f"{I} Es un numero perfecto")
            I+=1
        else:
            I+=1
else:
    print("fin del programa")
