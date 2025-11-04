# EJER 1
texto = " Isto é Python!"
print("longitud:", len(texto))


# EJER 2
palabra = "Python"
for caracter in palabra:
    print(caracter)


# Ejer 3

texto = "Python para todos"
texto_inv = texto[::-1]
print(texto_inv)


# EJER 4

texto = "Guido Van Rossum creou Python"
texto_sin = texto.replace(" ", "")
print(texto_sin)


# EJER 5

texto = "Python Python Python"
vocales = "aeiouAEIOU"
cons = 0
voc = 0

for caracter in texto:
    if caracter != " ":
        if caracter in vocales:
            voc += 1
        else:
            cons += 1

print("Número de vocais:", voc)
print("Número de consoantes:", cons)


# EJER 6

cadena = "www. phytonparatodos. com"
parte1 = cadena[:12]
parte2 = cadena[12:].strip()
print("parte 1: " + parte1)
print("parte 2: " + parte2)
nueva = parte1 + parte2
print(nueva)


# EJER 7

cadena = "Pythoneros"
cadena_mayus = cadena.upper()
print("Mayúsculas:", cadena_mayus)
cadena_minus = cadena_mayus.lower()
print("Minúsculas:", cadena_minus)


# EJER 8

cad1 = "Python"
cad2 = "JavaScript"

if cad1 == cad2:
    print("son iguales")
else:
    print("son diferentes")


# EJER 9

cad = "Jeve jeve jeve"
cad_mod = cad.replace("e", "a")
print(cad_mod)

def verificarFormatoData(data):
    verificacion = False
    data = data.strip()
    if len(data) == 10:
        if data[2] == '/' and data[5] == '/':
            dataseparada = data.split('/')
            if partes_con_longitudes_validas(dataseparada):
                if dataseparada[0].isdecimal() and dataseparada[1].isdecimal() and dataseparada[2].isdecimal():
                    dia = int(dataseparada[0])
                    mes = int(dataseparada[1])
                    ano = int(dataseparada[2])
                    if 1 <= dia <= 31 and 1 <= mes <= 12 and ano >= 1900:
                        verificacion = True
    return verificacion

def partes_con_longitudes_validas(partes: list[str]) -> bool:
    return (
        len(partes) == 3
        and len(partes[0]) == 2
        and len(partes[1]) == 2
        and len(partes[2]) == 4
    )

print(verificarFormatoData("29/02/2020"))
print(verificarFormatoData("31/04/2021"))
print(verificarFormatoData("15-08-1947"))


# EJER 10

s = "Ola, son alumno de DAM1, e son programador desde o 2025"
letras = sum(1 for c in s if c.isalpha())
digitos = sum(1 for c in s if c.isdigit())
espazos = sum(1 for c in s if c.isspace())

print("Cadea:", s)
print("Letras:", letras)
print("Díxitos:", digitos)
print("Espazos en branco:", espazos)
