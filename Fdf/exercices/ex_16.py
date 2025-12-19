# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex_16.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: equintas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/19 17:36:15 by equintas          #+#    #+#              #
#    Updated: 2025/12/19 17:36:17 by equintas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def find_max(a, b):
    if a > b:
        return (a)
    else:
        return (b)


num_1 = int(input("Digite um número: "))
num_2 = int(input("Digite um número: "))
print ("O maior número é: ", find_max(num_1, num_2))