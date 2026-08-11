paises = ["Angola", "Portugal", "Brasil", "Moçambique"]

dados_planta = ["Rosa", 23, 23.5, True]
paises.append("Argentina")
paises.insert(4, "Espanha")
paises.extend(["França", "Inglaterra"])

for indice, nome in enumerate(paises):
    print (f"{indice}- {nome}")

paises.pop()
paises.pop(1)
paises.remove("Moçambique")
paises.clear()
paises = ["Angola", "Portugal", "Brasil", "Moçambique"]
print (type(paises))
print (paises)
print (dados_planta)

paises.sort()
print (paises)

numeros = [1, 3, 0, -5, 45, 35, -2423, 24, 3245, 5343]
print(numeros)
numeros.sort()

print(numeros)
print(f"A lista possue {numeros.count(4)} elementos 4")

numeros.reverse()
print(numeros)

print (f"O número -5 está {numeros.index(-5)}* posição")

impares = [x for x in range(20) if x % 2 != 0]
print(impares)

clubes = ("FC Barcelona", "Real Madrid", "Bayern Munique", "AC Milan", "FC Liverpool")
print(clubes)
print(type(clubes))

melhor, maior, intimidante, baixou, mau = clubes
print(f"O melhor clube é: {melhor}")
print(f"O maior clube é: {maior}") 
print(f"O clube intimidante é: {intimidante}")
print(f"O clube que baixou é: {baixou}")
print(f"O clube mau é: {mau}")  

num = {1, 2, 3, 3, 2, 1}
print(num)
num = {4}
print(num)
num.add(3)
print(num)
num.update([2, 6, 10])
print(num)
num.remove(10)
print(num)
num.discard(15)
print(num)
n = num.pop()
print(n)
print(num)
num.clear()
print(num)

set_a = {1, 3, 4, 5, 6, 9, 10}
set_b = {0, 1, 2, 4, 5, 7, 10}

print (f"União: {set_a | set_b}")
print (f"Interseção: {set_a & set_b}")
print (f"Diferença: {set_a - set_b}")
print (f"Diferença simétrica: {set_a ^ set_b}")

num = frozenset([1, 10, 100])
print (num)
