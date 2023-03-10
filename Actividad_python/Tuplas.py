# Tuplas

print("Acceder a los elementos de una tupla utilizando el índice ")
tupla = (1, 2, 3, 4, 5)
print(tupla[0])
print(tupla[3])

print("Crear una tupla a partir de una lista utilizando la función tuple()")
tupla1 = [1, 2, 3, 4, 5]
tupla1 = tuple(tupla1)
print(tupla1)

print("Desempacar los elementos de una tupla en variables separadas ")
tupla2 = (1, 2, 3)
a, b, c = tupla2
print(a)
print(b)
print(c)

print("Obtener la longitud de una tupla utilizando la función len()")
tupla3 = (1, 2, 3, 4, 5)
print(len(tupla3))

print("Buscar el índice de un elemento en una tupla utilizando el método index() ")
tupla4 = (1, 2, 3, 4, 5)
print(tupla4.index(3))

print("Comprobar si un elemento está en una tupla utilizando el operador in ")
tupla5 = (1, 2, 3, 4, 5)
print(3 in tupla5)
print(6 in tupla5)