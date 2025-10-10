print("Ejer1")
n = int(input("num: "))
if n > 0:
  print("POSITIVO")




print("Ejer2")
a = int(input("primer num: "))
b = int(input("segundo num: "))
if a >= b:
  print("La resta es:", a - b)
print("La suma es:", a + b)




print("Ejer3")
a = int(input("num: "))
if a > 0:
  print("+")
if a < 0:
  print("-")
if a == 0:
  print("0")




print("Ejer4")
nombre1 = input("nom1: ")
peso1 = float(input("peso1: "))
nombre2 = input("nom2: ")
peso2 = float(input("peso2: "))


if peso1 > peso2:
  print(nombre1, peso1, "kg")
  print("dif:", peso1 - peso2, "kg")
else:
  print(nombre2, peso2, "kg")
  print("dif:", peso2 - peso1, "kg")




print("Ejer5")
a = float(input("num1: "))
b = float(input("num2: "))
c = float(input("num3: "))


if a > b and a > c:
  print("El mayor es:", a)
elif b > c:
  print("El mayor es:", b)
else:
  print("El mayor es:", c)
