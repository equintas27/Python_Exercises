# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex_15.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: equintas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/19 16:36:15 by equintas          #+#    #+#              #
#    Updated: 2025/12/19 16:36:17 by equintas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

lista_pessoas = []


for i in range(3):
    pessoa = {}
    pessoa["nome"] = str(input("Digite seu nome: "))
    pessoa["peso"] = float(input("Digite o seu peso: "))
    pessoa["idade"] = int(input("Digite a sua idade: "))
    lista_pessoas.append(pessoa)
    print ()

print ("Dados das pessoas: ")
for pessoa in lista_pessoas:
    print ("Nome: ", pessoa["nome"])
    print ("Peso: ", pessoa["peso"])
    print ("Idade: ", pessoa["idade"])
    print ()
