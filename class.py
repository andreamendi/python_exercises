class Perro:
    def __init__(self,raza,nombre,sexo,ladrido):
        #E  xpepto los atributos de init, viven en toda la función
        #Las variables deben de quedar clases desde el INIT
        self.raza = raza
        self.nombre = nombre
        self.sexo = sexo
        self.ladrido = ladrido
    
    #Cada método es independiente de lógica
    def ladrar(self):
        return self.ladrido
        #No se puede hacer print, sino que sí queremos devolver algo, con RETURN

    def dar_amor(self):
        return "Da amor moviendo la cola el  {}".format(self.raza)
        #Sí se declara una variable aquí solo vivirá aquí y no mas.

lucas = Perro("San Bernardo","lucas","nino","gufff guffff")

js = Perro("Gran napolitano","js","nino","guhhhhf guhhhhf")



# print(lucas.ladrar())
# print(js.dar_amor())

#------------------------------------------------

class Persona:
    def __init__(self,nombre,edad,nacionalidad,estatura,ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.estatura = estatura
        self.ocupacion = ocupacion
    
    def saludar(self):
        return "{} te dice hola".format(self.nombre)
    
    def trabaja(self):
        return "sabias que {} ocupa su dia siendo {}".format(self.nombre, self.ocupacion)
    
    def es_de(self):
        return "{} es de {}".format(self.nombre,self.nacionalidad)

print("Dame un nombre de alguna persona")
nombre = input()
print("Dame la edad de la persona")
edad = input()
print("Dame la nacionalidad de la persona")
nacionalidad = input()
print("Dame la estatura de la persona")
estatura = input()
print("Dime que hace la persona")
ocupacion = input()

persona = Persona(nombre,edad,nacionalidad,estatura,ocupacion)


print(persona.saludar())
print(persona.trabaja())
print(persona.es_de())