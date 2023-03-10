# Lista
print("Acceder a los elementos de una lista ")

numeros = [1, 2, 3, 4, 5]
print(numeros[0])
print(numeros[3])

print("Modificar los elementos de una lista ")
numeros2 = [1, 2, 3, 4, 5]
numeros2[2] = 10
print(numeros2)

print("Agregar elementos a una lista utilizando el método append( ")
numeros3 = [1, 2, 3, 4, 5]
numeros3.append(6)
print(numeros2)

print("Concatenar dos listas utilizando el operador + ")
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(lista3)

print("Obtener la longitud de una lista utilizando la función len() ")
numeros4 = [1, 2, 3, 4, 5]
print(len(numeros4))

print("Ordenar una lista utilizando el método sort() ")
numeros5 = [1, 2, 3, 4, 5]
numeros5.remove(3)
print(numeros5)

print("Concatenar dos listas utilizando el operador + ")
numeros6 = [3, 1, 4, 2, 5]
numeros6.sort()
print(numeros6)

print("Buscar el índice de un elemento en una lista utilizando el método index() ")
numeros7 = [1, 2, 3, 4, 5]
print(numeros7.index(3))

print("Comprobar si un elemento está en una lista utilizando el operador in ")
numeros8 = [1, 2, 3, 4, 5]
print(3 in numeros8)
print(6 in numeros8)