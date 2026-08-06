x = 2024
id_original = id(x)
print (f"Valor inicial de x: {x}")
print (f"Endereço de memória inicial (id): {id_original}")
x = -4
id_novo = id(x)
print (f"Valor inicial de x: {x}")
print (f"Endereço de memória inicial (id): {id_novo}")

if id_original != id_novo:
    print ("Python é maluco")

y = 0b111
print (y)
z = 0o12
print(z)
a = 0xA
print(a)