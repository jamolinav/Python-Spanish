'''
    Actualiza los valores en diccionarios y listas

'''

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1.- Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
print ('-' * 10, '*', '-' * 10)
print (x)
x[1][0] = 15
print (x)
# 2.- Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
print ('-' * 10, '*', '-' * 10)
print (students)
students[0]['last_name'] = 'Bryant'
print (students)
# 3.- En el directorio sports_directory, cambia 'Messi' a 'Andres'
print ('-' * 10, '*', '-' * 10)
print (sports_directory)
sports_directory['soccer'][0] = 'Andres'
print (sports_directory)
# 4.- Camba el valor 20 en z a 30
print ('-' * 10, '*', '-' * 10)
print (z)
z[0]['y'] = 30
print (z)
###################################################################

'''
    Itera a través de una lista de diccionarios
    
'''
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(dict_):
    for i in dict_:
        linea = ''
        for key, value in i.items():
            linea += f'{key} - {value}, '
        print (linea[:-2])
print ('-' * 10, '*', '-' * 10)
iterateDictionary(students) 
# La salida debería ser: (Está bien si cada clave y valor quedan en dos líneas separadas)
# Bonus: Hacer que aparezcan exactamente así!
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


###################################################################

'''
    Obtén valores de una lista de diccionarios
    
'''
def iterateDictionary2(key_, dict_):
    for i in dict_:
        for key, value in i.items():
            if key == key_:
                print (value)
print ('-' * 10, '*', '-' * 10)
iterateDictionary2 ('first_name', students)
print ('-' * 10, '*', '-' * 10)
iterateDictionary2('last_name', students)

###################################################################

'''
    Itera a través de un diccionario con valores de listas
    
'''
def printInfo(some_dict):
    for key, value in some_dict.items():
        print (len(value), key.upper())
        for i in value:
            print (i)
        print('')

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
print ('-' * 10, '*', '-' * 10)
printInfo(dojo)


