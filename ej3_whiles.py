#Loops While
#Mientras algo sucede tu sigue.

#El ejercicio de abajo, imprime los pares del 0 al 100

# x = 0
# while x <= 100:
#   print(x)
#   x += 2

# lista2 = [2,3,4,8,6,7]

# i = 0
# while i < len(lista2):
#   lista2[i] += lista2[i]
#   i += 1

# print(lista2)


#Break rompe el loop, y sí encuentra lo que busca rompe, incluso sí después hay más cosas igual a lo que busca.

# lista3 = [4,6,2,3,5,7,8,9,7]

# i = 0
# while i < len(lista3):
#   if(lista3[i] == 3):
#     print("Encontré el 3, en la posición {}". format(i))
#     break
#   else:
#     print("Continuo buscando")
#     continue #Aquí es para para la ejecución de aquí, y lo vuelve al while. En esté caso es infinito.
#     print("Ya acabé")

#------------------

#  Hacer un programa que imprima la suma de los 100 primeros números.
total = 0
i = 0

for i in range(0,101):
  total += i
  i += 1 
print(total)


while i <= 100:
  total += i
  i += 1
print(total)

#------------------
# Hacer un pseudocódigo que imprima los numeros impares hasta el 100 y que imprima cuantos impares hay.

