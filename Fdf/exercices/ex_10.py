# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex_08.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: equintas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/16 17:31:58 by equintas          #+#    #+#              #
#    Updated: 2025/12/16 17:32:03 by equintas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


lst = []

soma = 0

for i in range(5):
    dado = int(input("Digite um número: "))
    lst.append(dado)
print ("A média dos elementos é: ", sum(lst) / 5)

for elem in range(5):
    print ("Os elementos da lista:", lst[elem])
print(len(lst))
print ("O segundo valor da lista é:", lst[1])
lst.insert(1, 20)
print ("O segundo valor da lista é:", lst[1])
#lst.extend([30, 40, 50])
for j in range(6):
    print ("Os elementos da lista:", lst[j])
print("\n")
print(len(lst))
#lst.pop(3)
print(len(lst))
for n in range(5):
    print ("Os elementos da lista:", lst[n])
#lst.remove(20)
print("\n")
for m in range(4):
    print ("Os elementos da lista:", lst[m])
#print(lst.index(2))
#print(lst.count(20))
lst.sort()
print(lst)
lst.reverse()
print(lst)
lst.clear()
print(lst)


lst = []
print ("----- DIGITE OS NOMES DA SUA FAMÍLIA -----")
for i in range(6):
    nome = str(input("Nome: "))
    lst.append(nome)

for j in range(6):
    print(lst[j])

lst = []

print("---- DIGITE NOMES DA CIDADE ----")

for i in range(3):
    cidade = str(input("Cidade: "))
    lst.append(cidade)

for j in range(3):
    print(lst[j])


lst = [2, 4, 6, 8, 10, 12, 14]

num = int(input("Digite um número: "))

if num in lst:
    print ("Encontrado")
else:
    print ("Não Encontrando")



lst = []

print("---- DIGITE 5 NOMES ----")

for i in range (5):
    nome = str(input("NOME:"))
    lst.append(nome)

num = int(input("Digite um número de 0 á 4: "))

lst.pop(num)
print(lst)


lst = []

valor = 1
while (valor != 0):
    valor = int(input("Digite um valor: "))
    lst.append(valor)
print (len(lst))
max = (len(lst) - 1)
lst.sort()
print ("O menor valor é:", lst[0])
print ("O maior valor é:", lst[max])

