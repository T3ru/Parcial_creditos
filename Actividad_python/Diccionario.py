#Diccionarios

#Crear
"""Crear un diccionario"""
nom = input("Nombre: ")
ed = input("Edad: ")
ciu = input("Ciudad: ")
dic = {'Nombre': nom, 'Edad': ed, 'Ciudad': ciu}
print(dic)

#Accediendo al diccionario
"""Accedemos al valor"""
print("Accedemos al valor")
print(dic['Nombre'])

#Agregar una nueva clave con valor
"""Agregamos una nueva clave y su valor"""
print("Agregamos una nueva clave y su valor")
pro = input("Profesion: ")
dic['profesion'] = pro
print(dic)

#Modificar
"""Modificamos un valor"""
print("Modificamos un valor")
nom = input("Nombre: ")
ed = input("Edad: ")
ciu = input("Ciudad: ")
dic = {'Nombre': nom, 'Edad': ed, 'Ciudad': ciu}
dic ['Edad'] = ed
print(dic)

#Eliminar
"""Eliminamos una clave"""
print("Eliminamos una clave")
del dic['Ciudad']
print(dic)

#Recorrer
for valor in dic.values():
    print(valor)
