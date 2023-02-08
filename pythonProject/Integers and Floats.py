#Task1

import math
heltal1 = int(input("Write in one number"))
heltal2 = int(input("write in one more number"))

print("the quota was " + str(heltal1 / heltal2) + "!")
print("the rest was " + str(heltal1 % heltal2))
print(str(heltal1), "/", str(heltal2), "=", (math.floor(heltal1 / heltal2)), "and", str(heltal1 % heltal2), "in rest")
print(" ")
print("MVH Adriaan")
print(" ")
print(" ")

#Task2 Nummer 1 och 2

number1 = int(input("write one full number"))
number2 = float(input("write one more number with decimals"))
print("the float of the full number became ", float(number1))
print("the int of the decimal became ", int(number2))

#det som händer är att integern blir en float och i en float tar man bort decimaler och eftersom man sedan gör den till
#en float finns inga decimaler då heller och integern har decimaler men sen blir en float som tar bort de decimalerna

#Task2 Nummer 3

x = 4.3

print("x = 4.3")
print(math.ceil(x))
print(math.floor(x))

#När man använder ceil avrundas talet uppåt oberoende av decimalerna.
#När man använder floor avrundas talet neråt oberoende av decimalerna.

#Task 2 Nummer 4

Num1 = float(input("Choose one decimal number"))
Num2 = int(Num1)
print("The lowest denominator you can divide your number with is")
print((math.gcd(Num2)))

#Task 2 Nummer 5

import decimal
print("The circumference of a cirkel with the Radius 10 is")
Radius = 10
Circumference = (10 * math.pi * 2)
Circumference1 = decimal.Decimal(Circumference)
print(Circumference1)
print(" ")

#Task 3

Num1 = int(input("Write the first number"))
Biggest = Num1
Second_Biggest = 0
Num2 = int(input("Write the second number"))
if Num2 >= Biggest:
    Biggest = Num2
    Second_Biggest = Num1
    print(Biggest, + Second_Biggest)
else:
    Second_Biggest = Num2
Num3 = int(input("Write the third number"))
if Num3 >= Biggest:
    Second_Biggest = Biggest
    Biggest = Num3
elif Num3 >= Second_Biggest:
    Second_Biggest = Num3
Num4 = int(input("Write the fourth number"))
if Num4 >= Biggest:
    Second_Biggest = Biggest
    Biggest = Num4
elif Num4 >= Second_Biggest:
    Second_Biggest = Num4

print(Second_Biggest, "is the second biggest number")

