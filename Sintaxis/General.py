# al imprimir esta linea de codigo tendremos que se alojan los elementos del arreglo en cada una de las variables

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Sumamos varias variables con solo las letras

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# =====================================================================

# Variables globales

x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()

# =====================================================================

# Si crea una variable con el mismo nombre dentro de una función, esta variable será local y solo se puede usar dentro de la función. La variable global con el mismo nombre quedará como estaba, global y con el valor original.

x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is " + x)

#================================================================
# con la palabra global hemos designado una variable en el ambito global así este dentro de una función

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
