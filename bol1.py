# Boletín 1

print("EJER 1")
print("a)", ((3 + 2) % 2 - 15) / 2 * 5)
print("b)", (6 + 6 / 7) + 35 / 2 - 8 * 5 / 4 * 2)
print("c)", 3 + 6 * 14 % 3)
print("d)", 8 + 7 * 3 + 4 * 6 / 2 % 4)
print("e)", 27 % 4 + 15 / 4)
print("f)", 37 / 42 - 2)
print("g)", 9 * 2 / 3 * 25 * 3)
print("h)", (7 * 3 - 4 * 4) * 2 / 4 * 2)



print("EJER 2")

invalidas = ["Salto- mortal", "salto + mortal", "2salto", '"salto"', "cantidade total"]
print("Inv:", invalidas)



print("EJER 3")
m, n, p, q, r, s, c, t, i = 5, 9, 2, 7, 1, 4, 100, 36, 69

ex_a = (m + n) / n
ex_b = ((m + n) / p) / ((p - r) / s)
ex_c = (m + 4) / (p - q)
ex_d = (c * r * t) / 100
ex_e = (m + n) / (p + q / r)
ex_f = (m / n) * (p + q)
ex_g = (n * (1 + i)**t * i) / ((1 + i)**t - 1)

print("a)", ex_a)
print("b)", ex_b)
print("c)", ex_c)
print("d)", ex_d)
print("e)", ex_e)
print("f)", ex_f)
print("g)", ex_g)



print("EJER 4")
print("a)", True and True == False)
print("b)", not False == True)
print("c)", (True and True) or False == True)
print("d)", (False or False) and False != True)
print("e)", (not (True and False)) == False)
print("f)", "12" + "12" == "24")
print("g)", "34" + "43" == "3443")



print("EJER 5")

# a)
i, j, k = 1, 0, 1
print("a)", i + k <= j - k * 3 and k >= 2)

# b)
i, j, k = 3, 2, -1
print("b)", i == 3 or j <= 2 and k > 0)

# c)
tipo, rede = 10, 7.5
print("c)", tipo < rede + 1.5)

# d)
ano = 1993
print("d)", ano % 400 == 0)

# e)
print("e)", 3 == 2 or 5 > 1 + 1)

# f)
print("f)", 5 - 2 > 4 and not (0.5 == 1 / 5))

# g)
a, b, c, d = 2, 5, 6, 10
print("g)", a >= b or a >= c and a < d)

# h)
print("h)", a + b < c and a + c < d or 2 * a < a + b)

# i)
print("i)", (not (a * b < d)) and (not (a * b < c)) or b + c <= d)
