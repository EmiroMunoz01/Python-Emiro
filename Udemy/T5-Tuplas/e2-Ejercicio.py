# Dada la siguiente tupla crear una lista que solo incluya los numeros menores a 5

numeros = (13, 1, 8, 3, 2, 5, 8)
menores_cinco = []


for i in numeros:
    if i < 5:
        menores_cinco.append(i)

print(menores_cinco)
