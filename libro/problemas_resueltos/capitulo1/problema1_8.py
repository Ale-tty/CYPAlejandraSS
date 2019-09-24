X1 = float (input ("Dime cual es el valor de x de tu primer coordenada "))
Y1 = float (input ("Dime cual es el valor de y de tu primer coordenada "))
X2 = float (input ("Dime cual es el valor de x de tu segunda coordenada "))
Y2 = float (input ("Dime cual es el valor de y de tu segunda coordenada ")) 
DIS = ((X1 - X2) **2 + (Y1-Y2)**2)**0.5
print (f"La distancia entre los puntos ({X1},{Y1}) y ({X2},{Y2}) es {DIS}")
