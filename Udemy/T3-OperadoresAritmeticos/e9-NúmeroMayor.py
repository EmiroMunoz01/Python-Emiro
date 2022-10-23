numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))


if numero1 > numero2:
    print(f'El numero {numero1} es mayor que el número {numero2}')
elif numero1 == numero2:
    print(f'El número {numero1} es IGUAL que el número {numero2}')
else:
    print(f'El numero {numero2} es mayor que el número {numero1}')
