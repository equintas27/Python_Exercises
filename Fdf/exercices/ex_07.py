# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex_07.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: equintas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/13 13:16:13 by equintas          #+#    #+#              #
#    Updated: 2025/12/13 13:16:19 by equintas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

i = 0
while (i < 10):
    print ("Angola\n")
    i += 1

i = 0
while (i < 20):
    if (i % 2 == 0):
        print (f"{i} é Par\n")
    else:
        print (f"{i} é Ímpar\n")
    i += 1

print ("Olá, seja bem-vindo(a)\n")

print (f"O valor decimal é: {10: d}\n")
print (f"O valor binário é: {10: b}\n")
print (f"O valor real é: {10: f}\n")

nome = "Eugênio"
print (f"O meu nome é: {nome}\n")
print (f"A minha idade é: {23: d}\n")
print (f"A minha altura é: {1.85: .2f}\n")

idade = int(input("Digite a sua idade:\n "))
print (f"A sua idade é: {idade: d}\n")

print("O meu prato preferido é:", input("Digite o seu prato preferido:\n "))

nome = str(input("Digite o seu nome:\n "))
telefone = str(input("Digite o seu telefone: \n"))
bi = int(input("Digite seu número do bilhete: \n"))

print("O meu nome é:", nome)
print("O meu número de telefone é:", telefone) 
print("O meu número bilhete de identidade é:", bi)

# A vida é uma festa!
'''
A vida é muito melhor com Jesus
'''

import math
import os

num = int(input("Digite  um número: \n"))
raiz = math.sqrt(num)
print("A sua raiz quadrada é: ", raiz)

directorio = os.getcwd()
print("O meiu directório é: ", directorio)

nota = float(input("Digite a nota: \n"))
if nota >= 7:
    print ("Aprovado")
else:
    print ("Reprovado")

