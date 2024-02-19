#lists

my_list = list()
my_other_list = []

print(len(my_list))
my_list =[35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, 'Victor', 'Moreno']
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])

'''contar elementos dentro de una lista'''
print(my_other_list.count('Victor'))
print(my_list.count(30))
age, height, name, last_name = my_other_list
print(name)

print(my_list + my_other_list)
my_list = 'hola python'
print(my_list)
print(type(my_list))

my_other_list.append('Major17')
print(my_other_list)

my_other_list.insert(1, 'Azul')
print(my_other_list)

my_other_list.remove('Azul')
print(my_other_list)

my_list = list()

print(my_list)

my_other_list [1] = 'Rojo'
print(my_other_list)




