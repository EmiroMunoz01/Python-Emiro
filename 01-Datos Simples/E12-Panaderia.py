# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.


barrasDelDia = int(input("Ingrese el número de barras de pan vendidas: "))

precioOriginal = 3.49 * barrasDelDia
totalPrecio = (3.49 * barrasDelDia) * 0.4

print("El precio original de las", barrasDelDia,
      "barras de pan es de: ", precioOriginal, "€")
print("El precio con el descuento de las", barrasDelDia,
      "barras de pan es de: ", totalPrecio, "€")
print("La perdida monetaria de las", barrasDelDia,
      "barras de pan es de: ", (precioOriginal-totalPrecio), "€")
