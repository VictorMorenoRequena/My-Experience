'''Strings'''

my_string = 'My string'
my_other_String = 'My other string'
print(len(my_string))
print(len(my_other_String))

my_new_line_string = 'Este es un string \n con salto de linea'
print(my_new_line_string)

my_tab_string = 'Este es un string \t con salto de linea'
print(my_tab_string)

my_scape_string = 'Este es un  \nstring \t escapado'
print(my_scape_string)

#formateo

name, surname, age = 'Victor', 'Moreno', 35
print('My name is {} {}, y mi edad es {}'.format(name, surname, age)) 
print('My name is %s %s y mi edad es %d'%(name, surname, age)) #usar este
print(f'My name is {name} {surname}, y mi edad es {age}')

'''Desempaquetado de caracteres'''

language = 'Python'
a, b, c , d , e, f = language
print(a)
print(e)

#división

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

#reverse

reversed_language = language[::-1]
print(reversed_language)

language_slice = language[0:6:2]
print(language_slice)

#FUNCIONES DEL SISTEMA

print(language.capitalize())
print(language.upper())
print(language.count('t'))
print(language.isnumeric())
print('1'.isnumeric())
print(language.upper().isupper())
print(language.startswith('Py'))



