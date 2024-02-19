# Dictionaries

my_dict = dict()
print(type(my_dict))

my_other_dict = {}
print(type(my_other_dict))

my_other_dict = {'Nombre': 'Victor', 'Apellido': 'Moreno', 'Edad':23, 1:'Python'}
my_dict = {
    'Nombre': 'Victor', 
    'Apellido': 'Moreno', 
    'Edad':23, 
    'Languages': ('Python', 'Swift', 'Kotlin'),
    1:1.77
    }

print(my_dict)
print(my_other_dict)
print(my_dict['Nombre']) #Buscar dentro del diccionario

my_dict['Nombre'] = 'Pedro'
print(my_dict['Nombre'])

my_dict['calle'] = 'Eliseu' #añadir
print(my_dict)  

del my_dict['calle']
print(my_dict)

print('Moreno' in my_dict)
print('Apellido' in my_dict)
print('Morena' in my_dict)

print(my_dict.items())
print(my_other_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ['Nombre', 1, 'Piso']
My_New_Dict = dict.fromkeys((my_list))

My_New_Dict = dict.fromkeys((my_dict))
print((My_New_Dict))

My_New_Dict = dict.fromkeys(my_dict, ('Brais', 'Moure'))
print(My_New_Dict)
#My_New_Dict = my_other_dict.fromkeys(('Nombre', 1, 'Piso')) #No nos vale 
