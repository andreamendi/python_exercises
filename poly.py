class Animal:
    def __init__(self,sexo):
        self.sexo= sexo
    def comunicarse(self):
        raise NotImplementedError ("Subclass must implement abstract method")

class Perro(Animal):
    def __init__(self,sexo,raza):
        Animal.__init__(self,sexo)
        self.raza = raza
    def comunicarse(self):
        return "guaf guaf"

class Gato(Animal):
    def __init__(self,sexo,vidas):
        Animal.__init__(self,sexo)
        self.vidas = vidas

    def comunicarse(self):
        return "miaw miaw"

animal1 = Perro("niña","G danes")
animal2 = Gato("niño",7)

print(animal1.comunicarse())
print(animal2.vidas)
print(animal2.comunicarse())