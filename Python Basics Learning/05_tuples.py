#Tuples

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, 'Victor', 'Moreno')
my_other_tuple = (35, 60, 30)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])


print(my_tuple.count('Victor'))
print(my_tuple.count('Isco')) #Como no esta en la lista devuelve 0.
print(my_tuple.index('Victor'))#te dice la posicion de la primera coincidencia.

#my_tuple[1] = 1.80
#print(my_tuple) #En las tuples los valores no son a¡variables, por lo tanto no se pueden cambiar.

print(my_tuple + my_other_tuple) #
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple = tuple(my_tuple)

del my_tuple
#print(my_tuple) error

