#Write a map function that allow you convert a list of temperatures in Celsius to fahrenheit and viceversa
temperature = [14,12,17,5,6]


def fahrenheit (tem):
    fahrenheit = (tem * 1.8) + 32
    return round(fahrenheit) 

list(map(fahrenheit,temperature))
f = list(map(fahrenheit,temperature))

def celsius (tem):
    celsius = (tem - 32) / 1.8
    return round(celsius)
    
#list(map(celsius,f))

print(f)


#------------
num = [12,5,2,4,7,8,9,2,4,5,9,10]

def cinco(cin):
    return cin <= 5

list(filter(cinco,num))