# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: equintas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/26 15:10:47 by equintas          #+#    #+#              #
#    Updated: 2026/06/19 17:58:57 by equintas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from classes import Planta

def ft_plant_factory():
    plantas = [
        Planta("Rose", 25, 30),
        Planta("Dak", 200, 365),
        Planta("Cactus", 5, 90),
        Planta("Sunflower", 80, 45),
        Planta("Fern", 15, 120)
    ]
    for planta in plantas:
        planta.show()
        
if __name__ == "__main__":
    ft_plant_factory()
        
