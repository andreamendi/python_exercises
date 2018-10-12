#Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
import math

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2  =coor2

    def distance(self):
        raiz = math.sqrt((self.coor2[0]-self.coor1[0])**2+(self.coor2[1]-self.coor1[1])**2)
        return raiz
    def slope(self):
        slope = ((self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0]))
        return slope

coordinate1 = (3,2)
coordinate2 = (8,10)
li = Line(coor1=coordinate1,coor2=coordinate2)
li.distance()
print("Distancia {}".format(round(li.distance(),2)))
print("Slope {}".format(li.slope()))

#------------------------------
class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
    
    def surface_area(self):
       return (2 * math.pi * self.radius * self.height) + (2 * self.circle_area())

    def circle_area(self):
       return math.pi * self.radius**2

    def volume(self):
        return self.circle_area() * self.height
    
    

c = Cylinder(2,3)
print("Area de la base circular {}".format(round(c.surface_area(),2)))
print("Volumen {}".format(round(c.volume(),2)))

