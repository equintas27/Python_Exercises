# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: equintas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/09 16:50:59 by equintas          #+#    #+#              #
#    Updated: 2026/01/09 16:51:03 by equintas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_haverst_iterative():
    i = int(input("Days until harvest: "))
    for a in range(1, i + 1):
        print(f"Day: {a}")
    print ("Harvest time!")
    
ft_count_haverst_iterative()
