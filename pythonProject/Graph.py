
import random
import matplotlib.pyplot as mlt
import numpy as nmpi

min_value = int(input("Write the minimum number "))
max_value = int(input("Write the maximum number "))
Guess = int(input("choose one random number between them "))

ypoints1 = []
xpoints = []
ypoints2 = []

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
            ypoints2.append(Guess)
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
xnumber = nmpi.array(xpoints)
ynumber1 = nmpi.array(ypoints1)
ynumber2 = nmpi.array(ypoints2)


mlt.plot(xnumber,ynumber1,ynumber2)
mlt.show()

