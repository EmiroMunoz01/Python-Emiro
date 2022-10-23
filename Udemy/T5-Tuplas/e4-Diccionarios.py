# diccionario almacena una coleccion de datos con formato llave y valor, como esta en un diccionario real

diccionario = {
    'Nombre': 'Emiro',
    'Edad': 21,
    'Apellido': 'Muñoz',
    'Origen': 'Pitalito',
    'Altura': 1.84
}
print(diccionario)

# de esta forma conoceremos el tamaño del diccionario
print(len(diccionario))

# un diccionario es similar a un set, no se tienen indices dentro del diccionario, para acceder a un elemento debemos indicar la llave

print(diccionario['Nombre'])

# tambien tenemos otra forma
print(diccionario.get('Nombre'))

# modificaremos elementos dentro de un diccionario
diccionario['Nombre'] = 'Emirooo'
print(diccionario.get('Nombre'))


print(diccionario)

print("********************")
# recorreremos un diccionario con su llave y valor

for termino in diccionario.items():
    print(termino)

print("********************")

# aqui recorreremos el diccionario con solo su valor

for termino in diccionario.values():
    print(termino)
print("********************")

#ahora queremos recorrer solo las llaves

for termino in diccionario.keys():
    print(termino)

#tambien podremos comprobar la existencia de un elemento, en este caso de una llave

print("Edad" in diccionario)

#si queremos agregar un elemento

diccionario['PK'] = 'Primary Key'



print(diccionario)

#si queremos remover un elemento lo hacemos de la siguiente manera

#de esta forma hemos eliminado este elemento que indicamos
diccionario.pop("PK")
print(diccionario)

#ahora limpiaremos el diccionario
diccionario.clear()

#con este metodo eliminaremos la variable diccionario por completo

del diccionario


