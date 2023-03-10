#Estructuras selectivas
"""EJEMPLO IF"""
print("EJEMPLO IF")
nda = int(input("Nivel de astigmatismo: "))
if nda >= 3:
  print("Dioptrías alta")
  print(nda)

"""EJEMPLO DE IF Y ELSE"""
print("EJEMPLO DE IF Y ELSE")
nda2 = int(input("Nivel de astigmatismo "))

if nda2 >=3:
  print("Dioptrías alta")
else:
  print("Es una dioptria Media o baja")
print(nda2)

#Caso especial
"""EJEMPLO CASO ESPECIAL"""
print("EJEMPLO CASO ESPECIAL")
nda3 = int(input("Nivel de astigmatismo "))
if nda3 > 3:
  print("Dioptrías alta")
elif nda3 > 1.50 and nda3 < 2.75:
  print("Dioptrías media")
else:
  print("Dioptrías baja")
print(nda3)

#Estructuras repetitivas
"""EJEMPLO REPETITIVOS"""
print("EJEMPLO REPETITIVOS")
print("Ejemplo WHILE")
i = 1
while i <= 3:
  print(i)
  i += 1
print("Ejemplo FOR")
for i in range(1, 8):
  print(i)


