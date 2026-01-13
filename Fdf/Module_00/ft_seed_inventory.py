# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: equintas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/13 16:55:36 by equintas          #+#    #+#              #
#    Updated: 2026/01/13 16:55:52 by equintas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, qtd: int, unit: str)->None:
    if unit == "packets":
        print (f"{seed_type.capitalize()} {qtd} {unit} available")
    elif unit == "grams":
        print (f"{seed_type.capitalize()} {qtd} {unit} total")
    elif unit == "area":
        print (f"{seed_type.capitalize()} {qtd} {unit} square meters")
    else:
        print ("Error")

ft_seed_inventory("tomate", 23, "na")