SUE = float (input ("Introduce cuanto es tu sueldo "))
CATE = int (input ("Introduce cual es su categoria de empleado "))
HE = int (input ("Cuantas horas extra trabajo? "))
PHE = 0
NSUE = 0 
if CATE == 1: 
    PHE = 30 
elif CATE == 2:
    PHE = 38
elif CATE == 3: 
    PHE = 50 
elif CATE == 4: 
    PHE = 70 
else: 
    PHE = 0 
if HE > 30: 
    NSUE = SUE + 30 * PHE 
else: 
    NSUE = SUE + HE *PHE 
print (f"Este es su nuevo salario contemplando sus horas extra ${NSUE}")
