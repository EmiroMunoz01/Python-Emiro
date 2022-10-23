# Una tupla sigue guardando el orden de las listas, pero no podremos agregar, eliminar ni nada, sera inmutable

frutas = ('Naranja','Plátano','Guayaba','Manzana')
#Las funciones son muy similares, podremos saber el tamaño

print(len(frutas))
print(frutas)

#Podemos acceder a los elementos por el indice
print(frutas[0])

#También podemos acceder a los elementos con el -1, que sera el ultimo

print(frutas[-1])
print('*****************')
#Accederemos a un rango de valores
print(frutas [0:2])

#recorreremos la tupla con el ciclo for
print('*****************')

for fruta in frutas:
    print(fruta)

#podemos convertir una tupla en lista

frutaLista = list(frutas)
print(frutaLista)