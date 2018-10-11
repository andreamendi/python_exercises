# class Animal:
#     def __init__(self,estatura,peso,edad,f_comunicarse):
#         self.estatura = estatura
#         self.peso = peso
#         self.edad = edad
#         self.f_comunicarse = f_comunicarse

#     def comunicarse(self):
#         return self.f_comunicarse

# class Gato(Animal):
#     def __init__(self,estatura,peso,edad,f_comunicarse,vidas):
#         Animal.__init__(self,estatura,peso,edad,f_comunicarse)
#         self.vidas = vidas

#     def trepar(self):
#         print("estoy trepando")
    
#     def app(self):
        
    

#var = Gato(10,12,99,"miaw",0)
#print(var.comunicarse())


class Rrss:
    def __init__(self,nombre,color,leng_pro,app):
        self.nombre = nombre
        self.color = color
        self.leng_pro = leng_pro
        self.app = app

    def tengo_app(self):
        return "{} tengo app".format(self.app)

    def nombre_app(self):
        return "tu app se llama {}".format(self.nombre)


class Instagram(Rrss):
    def __init__(self,nombre,color,leng_pro,app,fotos,insta_stories):
        Rrss.__init__(self,nombre,color,leng_pro,app)
        self.fotos = fotos
        self.insta_stories = insta_stories
    
    def photo(self):
        return "Puedes poner {} en tu InstaStory".format(self.insta_stories)


insta = Instagram("instagram","Morado","js","si","Fotos geniales","filtros cools")


print(insta.tengo_app())
print(insta.nombre_app())
