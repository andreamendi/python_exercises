myfile = open('text.txt',"a+")
#w+ -> write plus -> todo lo sobre escribe hasta el texto original 
#Incluso sí es un código ya fue, y no existe cmd z.


myfile.write("\nHola Mendi")



#Método read es para "leer" el archivo y le pone un apuntador al final ->y es "ya lo leí y ya no te lo voy a volver a leer".
# El permiso es "r"
print(myfile.read()) 



#Es para mandarlo a cierta posición.
#.seek(Posición), en donde va a volver a empezar 
#myfile.seek(0)


#readlines y los manda como arrys -> listas
print(myfile.readlines())


#Se debe de cerrar
myfile.close()
