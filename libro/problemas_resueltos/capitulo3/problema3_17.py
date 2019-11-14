I = 3
SP = 0
M = int (input("Meta el numero limite"))
if M >= 1:
    SP+= 1
    print ("Numero primo",1)
    if M >= 2:
        SP+= 1
        print ("Numero primo",2)
while I <= M:
    BAND = "V"
    J = 3
    while J < (I /2)and BAND == "V":
        if ( I % J)== 0:
            BAND = "F"
            J+= 2
        else:
            J+= 2
    else:
        if BAND == "V":
            print (f" {I} Es un numero primo")
            SP+= 1
            I+= 2 
        else:
            I+= 2
else:
    print (f"Entre 1 y M hay {SP} numeros primeros")
    
            
