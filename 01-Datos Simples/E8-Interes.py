# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

dinero = int(input("Ingrese la cantidad de dinero: "))
años = int(input("Ingrese el numero de años: "))
interesA = float(input("Interes, ejemplo 3%, solo escribir el numero: "))
interesA = interesA/100

calculo = float((dinero * (interesA + 1)*años))
print("El dinero obtenido en ", años, " años es de: " , calculo)
