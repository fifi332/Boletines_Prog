# EJER 1


for x in range(10, 21):
    print(x)

# EJER 2


Fahrenheit = float(input("grados Fahrenheit: "))
celsius = (5 / 9) * (Fahrenheit - 32)

print("En Celsius es:", celsius)

# EJER 3


print("Fahrenheit    celsius")
f = 0
while f <= 120:
    C = (5 / 9) * (f - 32)
    print(f, "       ", C)
    f = f + 10

# EJER 4


ini = int(input("num inicial: "))
fin = int(input("num final: "))

for num in range(ini, fin + 1):
    if num % 2 == 0:
        print(num)


# EJER 5
def num_tri(n):
    for i in range(1, n + 1):
        suma = 0
        for j in range(1, i + 1):
            suma += j
        print(i, "-", suma)


n = int(input("cuantos num tri quieres?"))
num_tri(n)

# EJER 6

import math
def factorial():
    m = int(input("¿Cuántos quieres?: "))

    for orden in range(1, m + 1):
        n = int(input("Valor " + str(orden) + ": "))
        resultado = 1

        for i in range(1, n + 1):
            resultado *= i

        print("Valor", orden, ":", n, "Factorial:", resultado)


factorial()

# EJER 7


for i in range(0, 7):
    for num in range(0, 7):
        print(i, "|", num)


# EJER 8
def ocho():
    n = int(input("valor maximo de n: "))
    for i in range(0, n + 1):
        for num in range(0, n + 1):
            print(i, "|", num)


print(ocho())


# EJER 9
def contar():
    negativos = 0
    positivos = 0
    ceros = 0

    print("Introduce 10 números enteiros:")
    for _ in range(10):
        num = int(input())
        if num < 0:
            negativos += 1
        elif num > 0:
            positivos += 1
        else:
            ceros += 1

    print("Negativos:", negativos)
    print("Positivos:", positivos)
    print("Ceros:", ceros)


contar()


# EJER 10
def area_rectangulo():
    base = -1
    altura = -1

    while base <= 0:
        base = int(input(" base positiva: "))
        if base <= 0:
            print("positiva.")

    while altura <= 0:
        altura = int(input("altura positiva: "))
        if altura <= 0:
            print("positiva.")

    area = base * altura
    print("area: ", area)


area_rectangulo()

# EJER 11
while True:
    numero = int(input("un numero (0 pa salir): "))
    if numero == 0:
        print("fin")
        break
    print("tabla de", numero, ":")
    for i in range(1, 11):
        print(str(numero) + " x " + str(i) + " = " + str(numero * i))
    print("-" * 25)