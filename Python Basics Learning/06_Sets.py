#Sets

my_set = set()
my_other_set = {}
print(type(my_other_set))

my_other_set = {'Victor', 'Moreno', 35}
print(type(my_other_set))

#En el momento que le metemos datos se convierte en un set

print(len(my_other_set))

my_other_set.add('Victhekicker')
print(my_other_set) #Un set no es una estructura ordenada

my_other_set.add('Moreno')
print(my_other_set) #Un set no admite repetidos

print('Mouri' in my_other_set)
print('Moreno' in my_other_set) #Se pueden relizar busquedas

my_other_set.remove('Victhekicker')
print(my_other_set) 

my_other_set.clear() #para vaciar el set
print(my_other_set)  

print(len(my_other_set))
#del my_other_set lo elimina.


my_set = {'Victor', 'Moreno', 'Requena'}
print(my_set)

my_list = list(my_set)
print(my_list)
print(type(my_list))
print(my_list[0])

my_other_set = {'Kotlin', 'Swift', 'Python'}
my_new_set = my_set.union(my_other_set)
print(my_new_set.union({'Javascript', 'Cis'})) #esto no se guarda porque lo hemos hecho solo para el print.

print(my_new_set.difference(my_set))