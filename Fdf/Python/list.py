paises = ["Angola", "Portugal", "Brasil", "Moçambique"]

dados_planta = ["Rosa", 23, 23.5, True]
paises.append("Argentina")
paises.insert(4, "Espanha")
paises.extend(["França", "Inglaterra"])

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