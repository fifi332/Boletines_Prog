# EJER 1

def clas(ventas):
    if ventas <= 100:
        return "baixo"
    elif ventas <= 500:
        return "medio"
    elif ventas <= 1000:
        return "alto"
    else:
        return "primeira necesidade"

def papi():
    nom = input("articulo: ")
    ventas = int(input("ventas: "))

    tipo = clas(ventas)
    print("el articulo '" + nom + "' es:", tipo)

papi()


# EJER 2

import math

def menu():
    print("MENU")
    print("1. Cuadrado")
    print("2. Triangulo")
    print("3. Circulo")

def cua(lado):
    area = lado * lado
    return area

def tri(base, altura):
    area = (base * altura) / 2
    return area

def cir(radio):
    area = math.pi * (radio * 2)
    return area

menu()
opcion = input("Escoje una: ")

if opcion == "1":
    lado = float(input("lado: "))
    print(cua(lado))

elif opcion == "2":
    base = float(input("base: "))
    altura = float(input("altura: "))
    print(tri(base, altura))

elif opcion == "3":
    radio = float(input("radio: "))
    print(cir(radio))

else:
    print("nop")


# EJER 3
num = float(input("un número: "))
abs = num if num >= 0 else -num
print("valor absoluto de", num, "es", abs)


# EJER 4

unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
especiales = ["once", "doce", "trece", "catorce", "quice", "dieciseis", "diecisiete", "dieciocho", "diecinueve"]

num = (int(input("numero del 1 al 99: ")))

if 1 <= num <= 9:
    print(unidades[num])
elif 10 <= num <= 19:
    if num == 10:
        print("diez")
    else:
        print(especiales[num - 11])
elif 20 <= num <= 29:
    if num == 20:
        print("veinte")
    else:
        print("veinti" + unidades[num - 20])
else:
    dec = num // 10
    uni = num % 10
    if uni == 0:
        print(decenas[dec])
    else:
        print(decenas[dec], "y", unidades[uni])


# EJER 5

def calcular_letra_dni(numero):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    resto = numero % 23
    letra = ""

    for i in range(len(letras)):
        if i == resto:
            letra = letras[i]
            break
    return letra

def papi():
    dni = int(input("el DNI: "))
    letra = calcular_letra_dni(dni)

    print("El DNI es:", str(dni) + letra)

papi()


