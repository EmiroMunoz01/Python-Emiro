# funcion sumar que recibe varios argumentos numericos

# con el *args estamos diciendole que estamos recibiendo una cantidad de parametros indefinidos

def sumar_valores(*args):
    resultado = 0
    # iteramos cada elemento, podremos recorrer como una tupla, puede ser cualquier nombre en vez de argss
    for valor in args:
        resultado += valor
    return resultado


# Llamaremos nuestra funcion
print(sumar_valores(3, 5, 9, 1))
