CAN1 = 0
CAN2 = 0
CAN3 = 0
CAN4 = 0
VOTO = int (input("Introduce para quien es tu voto "))
while VOTO != 0:
    if VOTO == 1:
        CAN1+= 1
    elif VOTO == 2:
        CAN2+= 1
    elif VOTO == 3:
        CAN3+= 1
    elif VOTO == 4:
        CAN4+= 1
    VOTO = int (input("Introduce tu voto"))
else:
    SUMV = CAN1 + CAN2 + CAN3 + CAN4
    POR1 = (CAN1 / SUMV) * 100
    POR2 = (CAN2 / SUMV) * 100
    POR3 = (CAN3 / SUMV) * 100
    POR4 = (CAN4 / SUMV) * 100
    print (f"Los votos del candidato 1 son {CAN1} y su porcentaje es de {POR1}")
    print (f"Los votos del candidato 2 son {CAN2} y su porcentaje es de {POR2}")
    print (f"Los votos del candidato 3 son {CAN3} y su porcentaje es de {POR3}")
    print (f"Los votos del candidato 4 son {CAN4} y su porcentaje es de {POR4}")
print ("Fin del programa")
