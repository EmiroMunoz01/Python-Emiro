#las listas y las tuplas mantienen orden, ahora miraremos los set, un set no tiene orden y tampoco permite almacenar elementos duplicados, tampoco modificar los elementos, pero si es posible agregar o eliminar elementos

#no tenemos indice del cual apoyarnos

planetas = {'Marte', 'Jupiter', 'Venus'}

print(planetas)

#También podrenos conocer el largo de planetas
print(len(planetas))

#Sabremos si el elemento esta dentro del set
print('Marte' in planetas)

#agregar elementos
planetas.add('Tierra')
print(planetas)

#no podemos tener elementos duplicados

planetas.add('Tierra')
print(planetas)

#tambien podemos eliminar elementos

planetas.remove('Marte')
print(planetas)

#en caso de que la palabra ya se halla eliminado y estamos intentando eliminarla de nuevo no nos marcara error
planetas.discard('Tierra')

#Con esto limpiamos el set y lo dejamos vacio
planetas.clear()

#con esto eliminamos por completo todo
del planetas


