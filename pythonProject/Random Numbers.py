
import random
import matplotlib.pyplot as mlt
import numpy as nmpi

Elementlist = ["Ted", "Barney", "Marshall", "Lily", "Robin"]

for Breathtaking in range(2):
    print(random.choices(Elementlist))

print(random.randint(0, 9))

print(random.random())

print(random.uniform(9.5, 80.5))

print(round(random.uniform(33.33, 66.66),2))

print(random.SystemRandom().uniform(5, 10))

print(" ")


min_value = int(input("Write the minimum number "))
max_value = int(input("Write the maximum number "))
Guess = int(input("choose one random number between them "))

ypoints1 = []
xpoints = []

def binary_search(Guess, min_value, max_value):
    tries = 0
    found = False

    if max_value < min_value:
        print("Maximum value must be bigger than the minimum value")
    elif Guess < min_value or Guess > max_value:
        print("The number must be between min_value and max_value")
    else:
        while min_value < max_value and not found:
            tries += 1
            xpoints.append(tries)
            mid_value = (min_value + max_value) // 2
            ypoints1.append(mid_value)
            if mid_value == Guess:
                found = True
            else:
                if Guess < mid_value:
                    max_value = mid_value - 1
                else:
                    min_value = mid_value + 1

            print([(min_value, max_value), (mid_value, Guess), tries])

        print("The number is:", str(Guess))
        print("Tries:", str(tries))

print(binary_search(Guess, min_value, max_value))

print(ypoints1)
print(xpoints)

#xnumber = nmpi.array(xpoints)
#ynumber1 = nmpi.array(ypoints1)
#ypoint2 = nmpi.array([Guess])

xnumber=nmpi.array([12,10,20,50])
ynumber1=nmpi.array([18,20,26,57])

print(xnumber)
print(ynumber1)

mlt.plot(xnumber,ynumber1)
mlt.show()

print(" ")

Max_number = 100
Good_number = random.randrange(Max_number)
Guess = int(input("Guess the number"))
number_of_Guesses = 0
while Guess != Good_number:
    if Guess < Good_number:
        print("Higher")
        Guess = int(input("Guess again: "))
        number_of_Guesses += 1
    elif Guess > Good_number:
        print("Lower")
        Guess = int(input("Guess again: "))
        number_of_Guesses += 1
    if Guess == Good_number:
        print("You win")
    if number_of_Guesses == 10:
        print("Game over")

print(" ")

import math

lowest_number = int(input("Enter Lower bound:- "))

highest_number = int(input("Enter Upper bound:- "))

x = random.randint(lowest_number, highest_number)
print("\n\tYou've only ",
      round(math.log(highest_number - lowest_number + 1, 2)),
      " chances to guess the integer!\n")


count = 0

while count < math.log(highest_number - lowest_number + 1, 2):
    count += 1

    guess = int(input("Guess a number:- "))

    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")

if count >= math.log(highest_number - lowest_number + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")

#Random

import random

Integerslist = []

for Great in range(0, 10):
    Numbers1 = random.randint(30, 50)
    Integerslist.append(Numbers1)

print(Integerslist)

Floatlist = []

for Awesome in range(0, 5):
    Numbers2 = random.uniform(1, 10)
    Floatlist.append(Numbers2)

print(Floatlist)

Gaussianlist = []

for Astounding in range(0, 7):
    Numbers3 = random.gauss(50, 25)
    Gaussianlist.append(Numbers3)

print(Gaussianlist)

Elementlist = ["Ted", "Barney", "Marshall", "Lily", "Robin"]

for Breathtaking in range(2):
    print(random.choices(Elementlist))

#Break

Number = 0

while Number <= 100:
    Number += 1
    print(Number)
    if Number > 49:
        break

#Try and Except

Integer = int(input("Skriv ett number "))
String = str(input("Skriv ett ord "))

try:
    print(Integer, String)
except:
    print("What is wrong with you! You can not add an integer to a string ")
try:
    print(12/0)
except:
    print("A number can not be divided by zero ")


