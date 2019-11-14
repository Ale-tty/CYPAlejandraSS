MAYPRO = 0
N = int(input("Introduc el numero de fabricas"))
if N <= 100:
    I = 1
    for I in range(1,N+1,1):
        FABRICA= int(input("Introduce la clave de la fabrica"))
        TOTANU = 0
        J = 1
        for J in range(1,13,1):
            MES = float(input("Introduce la produccion de la fabrica en el mes"))
            TOTANU+= MES
            if J == 7 and MES > 3000000:
                print (f"la fabrica {FABRICA}")
                J+= 1
            else:
                J+= 1
        else:
            if TOTANU > MAYPRO:
                MAYPRO = TOTANU
                CLAVE = FABRICA
                print (f"Prodcuccion anual de fabrica es {FABRICA} y se vendio ${TOTANU}")
                I+= 1
    else:
        print (f"Fabrica que maas produjo en el año {CLAVE} y la produccion fue de ${MAYPRO}")
else:
    print ("Error en el numero de fabricas")
