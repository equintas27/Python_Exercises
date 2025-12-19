# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex_05.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: equintas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/13 12:33:38 by equintas          #+#    #+#              #
#    Updated: 2025/12/13 12:33:41 by equintas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from math import sqrt
x_1 = int(input("Digite x1: "))
x_2 = int(input("Digite x2: "))
y_1 = int(input("Digite y1: "))
y_2 = int(input("Digite y2: "))

d = sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)

print(f"Valor da distância: {d:.2f}")
