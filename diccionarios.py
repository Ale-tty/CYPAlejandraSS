#diccionarios{'llave':'valor'}
alumno={'num_cta':'201647757473',
        'nombre':('Jose','Perez','Garcia'),
        'semestre':1,
        'promedio':0.0,
        'materias':['CyP','algebra','calculo','geometria','introICO'],
        'regular':True,
        'lagrimas_por_examen': 5,
        'direccion':{
            'calle':'Rancho Sequito',
            'colonia':'Impulsora Popular Avicola',
            'numero':1000,
            'cp':17570,
            'del_mun':'Nezahualcoyotl',
            'estado':{
                'id':15,
                'nombre':'Estado de mexico',
                'corto':'EdoMex'
                }
            }
        }

print(alumno['materias'][1].upper())
alumno['lagrimas_por_examen'] =10
print(alumno)
alumno['cursa_ingles']=True
print(alumno) 
"""
print(alumno['nombre'])
print(alumno)
print(alumno['nombre'][1])
print(alumno['direccion']['cp'])
print(alumno['direccion']['estado']['corto'])
print(alumno['materias'][3::])

mi_lista=[['a','b'],['c',10],['d',True]]
diccionario= dict(mi_lista)
print(diccionario) 
print(alumno['direccion']['estado']['nombre'][10::].upper())
"""
# Son mutables

alumno['cursa_ingles']=True
print(alumno)

# funcion keys ()

llaves = alumno.keys()
print(llaves)
for llave in llaves:
    print("----------")
    print(llave)
    print('...........')
    print(alumno[llave])
    print("+++++++++++")
#funcion values

for val in alumno.values():
    print('......')
    print(val)
    print('++++++++++++++++++')

#funcion items()
for elem in alumno.items():
    print('....')
    print(elem)
    print('++++++++')


