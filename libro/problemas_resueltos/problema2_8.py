COMPRA = float (input ("De cuanto fue tu compra? "))
PAGAR = 0
if COMPRA < 500 : 
    PAGAR = COMPRA
else: 
    if COMPRA <= 1000:
        PAGAR = COMPRA - (COMPRA * 0.5)
    else: 
        if COMPRA <= 7000: 
            PAGAR = COMPRA - (COMPRA * 0.11) 
        else: 
            if COMPRA <= 1500 :
                PAGAR = COMPRA - (COMPRA * 0.18) 
            else: 
                PAGAR = COMPRA - (COMPRA * 0.25) 
print (f"Debes de pagar ${PAGAR}") 
print ("Fin del programa")
