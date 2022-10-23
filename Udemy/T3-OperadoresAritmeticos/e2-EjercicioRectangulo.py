#Función de rectangulo para hallar su area y perimetro

def rectangulo():
    altura = int(input("Ingrese la altura en cm: "))
    ancho = int(input("Ingrese el ancho en cm: "))
    area = altura * ancho
    perimetro = (altura * 2) + (ancho * 2)

    
    print(f'***********\nArea: {area} \nPerimetro: {perimetro}\n***********')



rectangulo()
