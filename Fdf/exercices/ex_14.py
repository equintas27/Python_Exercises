# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex_14.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: equintas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/19 16:00:46 by equintas          #+#    #+#              #
#    Updated: 2025/12/19 16:00:48 by equintas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


pessoa = {
    "nome": "",
    "peso": 0.0,
    "idade": 0
}

print ("--- Dados da pessoa ---")
print ()
print ("Nome:", pessoa["nome"])
print ("Peso:", pessoa["peso"])
print ("Idade:", pessoa["idade"])

pessoa["nome"] = "Texto"
pessoa["peso"] = 99.9
pessoa["idade"] = 23
print ()

print ("Nome:", pessoa["nome"])
print ("Peso:", pessoa["peso"])
print ("Idade:", pessoa["idade"])
print ()

pessoa["nome"] = str(input("Digite seu nome: "))
pessoa["peso"] = float(input("Digite o seu peso: "))
pessoa["idade"] = int(input("Digite a sua idade: "))
print ()

print ("Nome:", pessoa["nome"])
print ("Peso:", pessoa["peso"])
print ("Idade:", pessoa["idade"])
print ()