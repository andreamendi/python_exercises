import sys

text = (sys.argv)

try:
    myfile = open(text[1], "r")
    she = myfile.readlines()
    she.reverse()
    print(she)
    myfile.close()
except IndexError:
    print("Lo siento el archivo no existe")

except FileNotFoundError:
    print("Lo siento el archivo no esta bien escrito")

else:
    ("Lo lamento no es posible")