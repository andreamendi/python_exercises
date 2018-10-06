# Ejercicios  
# Tuve problemas con: 
# En el pseudocódigo: loop4 


# print("1")
# 1
# Hacer un pseudocodigo que imprima los numeros del 1 al 100. 
# for i in range(0,101):
#   print(i)

# print("\n")


# print("2")
# 2
# Hacer un pseudocodigo que imprima los números del 100 al 0, en orden decreciente.
# u = 100

# while u>0:
#   print(u)
#   u -= 1

# print("\n")


# print("3")
# 3
# Hacer un pseudocodigo que imprima los numeros pares entre 0 y 100.
# for n in range(2,100,2):
#    print(n)

# print("\n")


# print("4")
# 4
# Hacer un programa que imprima la suma de los 100 primeros números.
# total = 0
# k = 0

# for k in range(0,101):
#   total += k
#   k += 1 
# print(total)

# while k <= 100:
#   total += k
#   k += 1
# print(total)


# print("\n")

# print("5")
# 5
# Hacer un código que imprima los números impares hasta el 100 y que imprima cuantos impares hay.
# non = 0
# w = 0
# while w <= 100:
#   if w % 2 != 0:
#     print(w)
#     w += 1
#     non += 1
#   else:
#     w += 1
# print("En total son {}".format(non))

# print("\n")

# print("6")
# 6
# Hacer un pseudocodigo que imprima todos los numeros naturales que hay desde la unidad hasta un numero que introducimos por teclado
# print("Ingresa un numero")
# t=int(input())
# r = 1
# while r <= t:
#   print(r)
#   r += 1

# for r in range(1,t+1):
#   print(r)
#   r += 1

# print("7")
# 7
# Introducir tantas frases como queramos y contarlas. 

# lista_frases = []
# frase = ""
# u = 0
# veces = 0

# while frase != "fin":
#   print("Escribe algo que quieras. Si deseas salir, escribe 'fin'")
#   frase = input()
#   lista_frases.append(frase)
#   veces += 1
  
# print("Imprimiste {} numero de veces".format(veces))

# print("8")
# 8
# Hacer un pseudocodigo que solo nos permita introducir SI o NO y Si la respuesta es SI termine la ejecución y 
# si es NO pregunte de nuevo hasta que la respuesta sea SI.
# sino = "no"


# while sino == "no":
#   if sino == "si" or sino == "no":
#     print("Quieres salir de aqui?")
#     sino=input()
#   else: 
#     print("Lo lamento, no lo leo.")



# print("9")
# 9
# Imprimir y contar los multiplos de 3 desde la unidad hasta un numero que introducimos por teclado.
# y = 1
# print("Digita un numero")
# numero=int(input())
# o = 0
# while y <= numero:  
#   print (y)

  
# while y <= numero:
#   if y % 3 == 0:
#     print (y)
#     o += 1

#   y += 1
# print("En total fueron: {}".format(o))



# print("10")
# 10
# Hacer un pseudocodigo que imprima los numeros del 1 al 100. Que calcule la suma de todos los numeros 
# pares por un lado, y por otro, la de todos los impares. 
# total = 0
# total_par = 0
# total_non = 0
# r = 1

# while r <= 100:
#   if r % 2 == 0:
#     total_par += r
#     total += r
#     r += 1
#   else:
#     total_non += r
#     total += r
#     r += 1

# print("Total de pares: {}".format(total_par))
# print("Total de nones: {}".format(total_non))
# print("Total de totales: {}".format(total))

print("11")
# 11
# Imprimir y contar los numeros que son multiplos de 2 o de 3 que hay entre 1 y 100.

total = 0
total_dos = 0
total_tres = 0
t = 1



while t <= 100:
  print("¿Multiplo de 2 'o 3?")
  dostres = int(input())
  if dostres % 2 == 0:
    total_dos += t
    total += t
    t += 1
  elif dostres % 3 == 0:
    total_tres += t
    total += t
    t += 1
  if dostres == 2:
    print("El total con un multiplo de: {} fue = {}".format(dostres,total_dos)
  elif dostres == 3:
    print("El total con un multiplo de: {} fue = {}".format(dostres,total_tres)
