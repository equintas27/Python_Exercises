# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex_12.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: equintas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/19 09:58:59 by equintas          #+#    #+#              #
#    Updated: 2025/12/19 09:59:02 by equintas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

mat = []

for linha in range(3):
    linha = []
    for num in range(3):
        linha.append(int(input()))
    mat.append(linha)
print(mat)


nome = str(input("Digite seu nome: "))
sobrenome = str(input("Digite seu sobrenome: "))

print ("O tamanho do nome:", len(nome))
print ("O tamanho do sobrenome:", len(sobrenome))


con_name = nome + " " + sobrenome
print ("O meu nome completo é: ", con_name)
print ("O tamanho do completo: ", len(con_name))



nomes = []

while 1:
    nome = str(input("Digite um nome ou /exit(para sair): \n"))
    if nome == "/exit":
        break
    nomes.append(nome)

con_nomes = " ".join(nomes)
print (con_nomes)



tupla = (0, 1, 3, 3, 5, 7, 7, 7)

print ("Conteúdo da tupla:", tupla)

print ("O tamanho da tupla é:", len(tupla))

print ("A quantidade de elementos iguais a 7 na tupla: ", tupla.count(7))

print ("Elemento da posição 4 (quinta pos): ", tupla[4])

frutas = ("maçã", "banana", "laranja")

for elem in frutas:
    print("Fruta: ", elem)
print("A quantidade de elementos na pilha são: ", len(frutas))


