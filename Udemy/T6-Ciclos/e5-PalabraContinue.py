# imprimiremos numeros pares dentro de un rango de datos

for i in range(10):
    if i % 2 == 0:
        print(f"valor: {i}")

# De esta forma tenemos los números pares
#si el valor de i no es divisible entre dos nos iremos a la siguiente linea que es la impresión
for i in range(10):
    if i % 2 != 0:
        continue
    print(f"valor: {i}")
