#Ejercicio 1

#if (1> 1):
#   print("hola")
#elif (1 ==1):
#    print("heola")
#else:
#    print("holdda") 


#Ejercicio 2

#lista = [2,3,4,5,6,7,8,9,9]
#lista2 = []
#for num in lista:
#    lista2.append(num * num)
#    print(num)
#    print(lista2)


#Ejercicio 3

#lista3 = [3,5,6,3.5,67,8,8]
#lista4 = []
#for i in lista3:
#    lista4.append(i)
#    var=set(lista4)
#    print(var)

#Ejercicio 4

# lista5 = [1,2,3,4,5,6,7,8,9,10]
# pares = [] 
# nones= []

# for numero in lista5:
#     if numero % 2 == 0:
#         pares.append(numero)
#     else:
#         nones.append(numero)
# print(pares)
# print(nones)
##lista[num-1] += i  

#índice indica en este caso indica la posición. 
#Por ejemplo en el ejercicio de abajo, inicia en 0.


#
lista6 = [2,3,4,8,6,7]
n = 0
for num in lista6:
  i = num + num
  lista6[n]=i
  n += 1
   
print(lista6)

