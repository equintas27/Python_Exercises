# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: equintas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/09 16:51:38 by equintas          #+#    #+#              #
#    Updated: 2026/01/09 16:51:42 by equintas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_contagem(dia, limit):
    if (dia > limit):
        return 
    print ("Day:", dia)
    ft_contagem (dia + 1, limit)

def ft_count_haverst_recursive():
    i = int(input("Days until harvest: "))
    ft_contagem (1, i)
    print ("Harvest time!")

ft_count_haverst_recursive()
