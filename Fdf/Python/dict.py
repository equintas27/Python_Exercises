Jogador = {
    "name": "Eugênio Quintas",
    "idade": 24,
    "peso": 1.95,
    "Posicao": "Avançado",
     "Clube": "FC Barcelona",
    "Dorsal": 9
}


print(Jogador)

for chave in Jogador.keys():
    print(chave)
for valor in Jogador.values():
    print(valor)
for chave, valor in Jogador.items():
    print (f"{chave}: {valor}")

print (Jogador["Clube"])
print (Jogador.get("peso"))

Jogador["Nacionalidade"] = "Angolana"
for chave, valor in Jogador.items():
    print (f"{chave}: {valor}")

Jogador1 = {
    "name": "Eugênio Quintas",
    "idade": 24,
    "peso": 1.95,
    "Posicao": "Avançado",
    "Dorsal": 9
}

Jogador2 = {
    "name": "Vanildo dos Santos",
    "idade": 21,
    "peso": 1.83,
    "Posicao": "Extremo",
    "Dorsal": 11
}

Jogador3 = {
    "name": "Domingos dos Santos",
    "idade": 12,
    "peso": 1.25,
    "Posicao": "Médio-Centro",
    "Dorsal": 10
}

Clubes = {
    "FC Barcelona" : Jogador1,
    "Real Madrid" : Jogador2,
    "FC Liverpool": Jogador3
}

for x, obj in Clubes.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])