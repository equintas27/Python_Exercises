# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: equintas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/13 17:43:09 by equintas          #+#    #+#              #
#    Updated: 2026/01/13 17:43:12 by equintas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_haverst_iterative():
    i = int(input("Days until harvest: "))
    for a in range(1, i + 1):
        print(f"Day: {a}")
    print ("Harvest time!")

def ft_contagem(dia, limit):
    if (dia > limit):
        return 
    print ("Day:", dia)
    ft_contagem (dia + 1, limit)

def ft_count_haverst_recursive():
    i = int(input("Days until harvest: "))
    ft_contagem (1, i)
    print ("Harvest time!")