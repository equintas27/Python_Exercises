import cmath

z = 3 + 4j
print (z)
z1 = 5j
print (z1)
z2 = -2.5 + 1.2j
print (z2)

z4 = complex(2)
print(z4)
z5 = complex(3, 5)
print (z5)

#Acessando as partes real e imaginária

z6 = 3 + 2j

print (z6.real)
print (z6.imag)

#Operations

a = 2 - 6j
b = 3 + 4j

print (f"Soma: {a + b}")
print (f"Subtração: {a - b}")
print (f"Multiplicação: {a * b}")
print (f"Divisão: {a / b}")

print(b.conjugate())
print(abs(b))

raiz = cmath.sqrt(-9)
print (raiz)