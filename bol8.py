#ejer 1
num1 = int(input("dime valor: "))
num2 = int(input("dime valor: "))
num3 = int(input("dime valor: "))
num4 = int(input("dime valor: "))


numeros = (num1, num2, num3, num4)


def ordenador():


 if numeros == tuple(sorted(numeros)):
     print("Ordenado de menor a maior")
 elif numeros == tuple(sorted(numeros, reverse=True)):
     print("Ordenado de maior a menor")
 else:
    print("esta desoredenado")


ordenador()


#ejer 2
def encajan(ficha1, ficha2):
    return ficha1[0] in ficha2 or ficha1[1] in ficha2


print(encajan((3, 5), (5, 2)))
print(encajan((1, 4), (2, 6)))


#ejer 3
def saludo(nombres):
    for nombre in nombres:
        trata = "doña " if nombre.endswith("a") else "don "
        print("Estimado " + trata + " " + nombre)


saludo(["Ana", "Luis", "Maria", "Carlos"])


#ejer 4
def saludo(nombres, p, n):
    selec = nombres[p:p+n]
    for  nombre in selec:
        trato = "dona" if nombre.endswith('a') else "don"
        print("Estimado " + trato + " " + nombre)


saludo(("Manuel", "Lucia", "Carlos", "Maria"), 0, 2)
