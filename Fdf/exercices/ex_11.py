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

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

print ("Elementos da primeira linha:")
for i in mat[0]:
    print(i, end=" ")

print()

print ("Todos os elementos de mat:")
for linha in mat:
    for elem in linha:
        print(elem, end=" ")
    print()
print ("Penúltimo elemento da matriz: ", mat[2][1])

mat2 = [
    [],
    [],
    []
]
for linha in mat2:
    for i in range(4):
        num = int(input("Digite um número: "))
        linha.append(num)
    print()

for l in mat2:
    for j in l:
        print (j, end=" ")
    print()

numbers = []
for lin in mat2:
    for r in lin:
        numbers.append(r)

print ("Max:", max(numbers))
print ("Min:", min(numbers))

