#PROBLEM 3


# Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.
def ask():
    
    while True:
          print("Dame un numero entero")
        try:
            number = int(input())
            print("cuadrado", number**2)
        except TypeError:
            print("Sorryyyyyy no es un numero int")
        except ValueError:
            print("Sorryyyyy")
