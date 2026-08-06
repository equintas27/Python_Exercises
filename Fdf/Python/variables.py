my_first_variable = 1

print(type(my_first_variable))
print(my_first_variable)

my_first_variable = "Eu amo a minha Angola"

print(type(my_first_variable))
print(my_first_variable)

import collections

my_first_variable = collections.Counter([1, 1, 2, 3, 3, 3, 3, 3, 4, 5, 6, 7])


print(type(my_first_variable))
print(my_first_variable)

def my_func():
    global y
    y = "EugênioQuintas"
my_func()

print ("Valor da variável global:", y)

x = "Angola"

def my_f():
    global x
    x = "Argentina"
my_f()

print ("My country is: " + x)
