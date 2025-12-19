# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex_06.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: equintas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/13 12:56:35 by equintas          #+#    #+#              #
#    Updated: 2025/12/13 12:56:38 by equintas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from math import sqrt
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = (b ** 2 - 4*a*c)
x1 = (-b + sqrt(delta)) / 2 * a
x2 = (-b + sqrt(delta)) / 2 * a
print (f"Valor de x1: {x1}")
print (f"Valor de x2: {x2}")