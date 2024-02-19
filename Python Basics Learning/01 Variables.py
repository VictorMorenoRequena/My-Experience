#Variables

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

#Cambiar tipo de dato, de num a str
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

#Concatenación de variables en un print
print(my_string_variable, str(my_int_variable), my_bool_variable)
print("Este es el valor de:", my_bool_variable)

#funciones del sistema

'''Counts the word length'''
print(len(my_int_to_str_variable))

'''Variables en una sola linea'''
name, surname, nickname, age = "Victor", "Moreno", 'Vickthekicker', 23
print('Me llamo', name, surname, 'me llaman', nickname, 'y mi edad es de', age)

'''inputs'''
first_name = input(' Whats your name? ')
last_name = input('and last name?' )
print(first_name)
print(last_name)



'''change type'''
first_name = 123
last_name = 456
print(first_name)
print(last_name)

'''Forzamos el tipo'''
adress: str = 'My adress'
adress = True
print(type(adress))





