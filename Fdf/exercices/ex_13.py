# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex_13.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: equintas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/19 14:19:07 by equintas          #+#    #+#              #
#    Updated: 2025/12/19 14:19:13 by equintas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


con_1 = {1, 2, 3, 4}

con_2 = {3, 4, 5, 6}

print(con_1)
print(con_2)

uni = con_1.union(con_2)
inte = con_1.intersection(con_2)
differ = con_1.difference(con_2)

print ("Resultado da união: ", uni)
print ("Resultado da intercessão: ", inte)
print ("Resultado da diferença: ", differ)

conj_1 = {"Carlos", "Josiel", "Jandira", "Aline"}
          
conj_2 = {"Aline", "Carlos", "Jaqueline", "Altair"}

interce = conj_1.intersection(conj_2)

differe = conj_1.difference(conj_2)

unionnn = conj_1.union(conj_2)

print (interce)
print (differe)
print (unionnn)