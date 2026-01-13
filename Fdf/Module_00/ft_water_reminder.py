# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: equintas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/09 16:42:34 by equintas          #+#    #+#              #
#    Updated: 2026/01/09 16:42:38 by equintas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    day = int(input("Days since last watering: "))
    if day > 2:
        print ("Water the plants!")
    else :
        print ("Plants are fine")
