# EJER 1


def notas():
    asignaturas = ["Mates", "Fisica", "Quimica", "Historia", "Lengua"]
    notas = []

    for asignatura in asignaturas:
        nota = input("¿Qué nota sacaste en " + asignatura + ": ")
        notas.append(nota)

    for i in range(len(asignaturas)):
        print("En", asignaturas[i], "has sacado", notas[i])


notas()


# EJER 2
def numeros_loteria():
    ganadores = []
    print("6 num ganadores de primitiva:")

    for i in range(6):
        num = int(input("Número " + str(i + 1) + ": "))
        ganadores.append(num)
    ganadores.sort()

    print("Números gañadores ordenados:", ganadores)


numeros_loteria()


# EJER 3
def inverso():
    num = list(range(1, 11))
    num.reverse()
    for i in range(len(num)):
        if i < len(num) - 1:
            print(num[i], end=",")
        else:
            print(num[i])


inverso()


# EJER 4
def notas():
    asignaturas = ["Mates", "Fisica", "Quimica", "Historia", "Lengua"]
    repetir = []

    for asignatura in asignaturas:
        nota = int(input("¿Qué nota sacaste en " + asignatura + ": "))
        if nota < 5:
            repetir.append(asignatura)

    print("Tienes que repetir:", ", ".join(repetir))


notas()

# EJER 5


abe = list(" abcdefghijklmnñopqrstuvwxyz")

res = [letra for i, letra in enumerate(abe) if i % 3 != 0]

print(res)


# EJER 6


def es_palindromo():
    palabra = input("una palabra: ")
    if palabra == palabra[::-1]:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")


es_palindromo()


# EJER 7
def contar_vocales(palabra):
    palabra = palabra.lower()
    vocales = "aeiou"

    for vocal in vocales:
        cantidad = palabra.count(vocal)
        print("La vocal '" + vocal + "' aparece " + str(cantidad) + " veces")


palabra_usuario = input("Introduce una palabra: ")

contar_vocales(palabra_usuario)

# EJER 8


pre = (50, 75, 46, 22, 80, 65, 8)

menor = min(pre)
mayor = max(pre)

print(menor, mayor)

# EJER 9


v1 = [1, 2, 3]

v2 = [-1, 0, 2]
producto_escalar = sum(a * b for a, b in zip(v1, v2))
print("El producto escalar es:", producto_escalar)
