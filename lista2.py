# arreglos 
#lectura 
#escritura/Asignacion 
# Actualizacion: insercion, eliminacion, modificacion 
#ordenamiento
#busqueda

#escritura
frutas = ["Zapote","Manzana", "Pera", "Aguacate", "Durazno", "Uva", "Sandia"]

# Lectura, el selector [indice]
print (frutas[2]) 

# Lectura con for
#for opcion 1
for indice in range (0,7,1):
    print (frutas[indice])
print ("-------")

# for opcion 2 -- por un iterador for each

for fr in frutas:
    print (fr)

# asignacion
frutas[2] = "Melon"
print (frutas) 
#insercion al final
#Agregar elementos 
frutas.append("Naranja")
print (frutas)
print(len(frutas))
frutas.insert(2, "Limon")
print (frutas) 
print (len(frutas))
frutas.insert(0,"Mamey")
print(frutas)
print(len(frutas))
#Eliminacion con pop
print(frutas.pop())
print(frutas)
print(frutas.pop(1))
print (frutas)
frutas[2] ="limon"
frutas.append("limon")
frutas.append("limon")
print (frutas)
frutas.remove("limon") 
print (frutas)

#ordenamiento
frutas.sort()
print (frutas) 
frutas.reverse()
print (frutas)

#busquedda
print (f"El Uva esta en la posicion. {frutas.index('Uva') }")
print (f"El limon esta {frutas.count('limon') } veces en la lista")

#Concatenar
print(frutas)
otras_frutas= ["Rambuta", "Mispero", "Lichie", "Pitahaya"]
frutas.extend (otras_frutas)
print (frutas)

#copiar

copia = frutas
copia.append("Naranja")
print (frutas)
print (copia)

otra_copia = frutas.copy()
otra_copia.append ("Fresa")
otra_copia.append ("Fresa")
print(frutas)
print (otra_copia) 
