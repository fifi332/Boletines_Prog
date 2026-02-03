import random

def generar_contraseña(longitud=8):
    if longitud < 6:
        longitud = 6
    if longitud > 18:
        longitud = 18

    mayus = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    minus = 'abcdefghijklmñopqrstuvwxyz'
    numeros = '0123456789'
    simbolos = '°|¬!#$%&/()=?¡¿+*~[]{};:,.<>'
    todos = mayus + minus + numeros + simbolos

    contraseña = ''
    for _ in range(longitud):
        con = random.randint(0, len(todos))
        contraseña += todos[con]
    return contraseña

while True:
    n = int(input("Ingrese la longitud de la contraseña (6-12): "))
    if n >= 6 and n <= 12:
        print(generar_contraseña(n))
    elif n == 0:
        break
    else:
        print("eres medio marico verdad?")

print(generar_contraseña(12))
