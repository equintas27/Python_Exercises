# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: equintas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/26 15:10:47 by equintas          #+#    #+#              #
#    Updated: 2026/05/26 15:53:53 by equintas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Planta:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"Created: {self.name}, {self.height} cm, {self.age} days old")
    def grow(self):
        self.height += 0.8
        self.height = round(self.height, 1)
    def age_old(self):
        self.age += 1

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
        
        
