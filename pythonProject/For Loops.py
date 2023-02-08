
friends =["Lucas", "Martin", "Gabriel", "Alfons", "Felix",]
for index in range(5):
    if index == 0:
        print("first Iteration")
    elif index == 2:
        print("third iteration")
    else:
        print("Not first")

#Task 1

word = ("Jensen")
parentheses1 = ("(")
parentheses2 = (")")
for letter in word:
    print(parentheses1 + letter + parentheses2)

#Task 2

Triangle = int(input("Write one number "))
Letter = " "
for number in range(Triangle):
    print("|" + (" " * number) + "\\")

#Task 4

Number1 = int(input("write one number"))
Amount = 0
for Thing in range(Number1):
    Thing += 1
    Amount+= Thing
print(Amount)

#Task 3   again

Square = int(input("Write one number "))
print(" " + "_" * (Square * 2))
for Info in range(Square):
    #print(" " + "_" * (Square * 2))
    if Info == Square-1:
        print((("|"  + "_" * (Square * 2)) + "|"))
    else:
        print("|" + (" " * (Square * 2) + "|"))

#Could not do 5 today. I will send it to you tomorrow

#Task 5

Number = int(input("Enter one number "))
Mumber = int(input("Enter another number "))






























