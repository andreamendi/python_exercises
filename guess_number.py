# Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
# If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# On a player's first turn, if their guess is 
# - within 10 of the number, return "WARM!"
# - further than 10 away from the number, return "COLD!"
# On all subsequent turns, if a guess is
# closer to the number than the previous guess return "WARMER!"
# farther from the number than the previous guess, return "COLDER!"
# When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
# You can try this from scratch, or follow the steps outlined below. A separate Solution notebook has been provided. Good luck!
 
import random
randy = random.randint(1, 100)
i = 1
print(randy)
print("\n")
prev_guess = 0

print("Hello!, we've ur secret number and is a random integer from 1 to 100, so plis guess than number. Have us a number and good luke!")
guess_user = int(input())

if guess_user == randy:
    print("Yeah u did it at the first time. Ur number was {}".format(randy))

while guess_user != randy:
    suma_prev = abs(int(guess_user) - randy)

    #print("suma prev{}".format(suma_prev))

    if guess_user <= 100 and guess_user >= 1:
        
        if i == 1:
            if  abs(randy - int(guess_user)) <= 10:
                print("WARM!")
                print("\n")
            else:
                print("COLD!")
                print("\n")
            i += 1

        else:
            print("Ups! Sorry, ur last number isn't correct")
            guess_user = int(input())
            suma_actual = abs(randy - int(guess_user))

            #sumas=abs(suma_prev - suma_actual)

            if guess_user == randy:
                print("Yeah! U did it. Your random secret number was: {} ".format(randy))
                print("And u try {} times".format(i-1))
            elif suma_actual <= suma_prev:
                print("WARMER!")
                #print("You're close at: {} numbers".format(suma_prev))
                print("\n")

            elif suma_actual >= suma_prev:
                print("COLDER!")
                print("\n")
        i += 1

    else:
        print("Sorry, your number isn't between 1 - 100, your random number was {}".format(randy))
        break



            

    

 