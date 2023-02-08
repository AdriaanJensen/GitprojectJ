
#Task1.2
variabel1 = 'a, b, c'
a = 10
alpha = True
variabel2 = a
variabel3 = 1
variabel4 = "b"
variablel5 = alpha

print(variabel1)
print(variabel2)
print(variabel3)
print(variabel4)
print(variablel5)

print(" ")

#Task 1.3
print(1/3)
print('1/3')
a = 1/3
print(a)
print('a')

#Task 1.4

adriaanAge = 18
adriaanHeight = 185
adriaanSchool = True
oliverAge = 72
oliverHeight = 425
oliverSchool = False
santeAge = 78
santeHeight = 57
santeSchool = True
print(adriaanAge, adriaanHeight, adriaanSchool)
print(oliverAge, oliverHeight, oliverSchool)
print(santeAge, santeHeight, santeSchool)


#Task 2.1

def beraknaArea(sida1, sida2):
   area = sida1*sida2
   return area

beraknaArea(2, 4)
def alternativtBeraknaArea(sida1, sida2):
   print(sida1*sida2)
   alternativtBeraknaArea(3, 15)
def adderaSiffror(siffra1, siffra2):
   summa = siffra1+siffra2
   return summa
def multiplicerasenAddera(x, y): #den hära multiplicerar x och y för att sedan addera y. den kan använda int och float
   a = x*y+y
   return a
def Addition(x, y):  #den här adderar x och y. den kan använda float och int
   print(x+y)

import numpy as np #låt denna vara, återkommer till import
def multipliceraochmultiplicerasenAddera(a, b):  #den här multiplicerar a med a och b med b sen adderas de. den använder float och int
  c = np.sqrt(a*a + b*b)
  return c

print(beraknaArea(3.5 , 4))

#Task 2.3

def process(fixed, current, remaining):  #den här funktionen kan skapa kombinationer mellan olika number som 1 och 2 eller 12
    if len(remaining) == 0:
        print("I got here 1")
        return [fixed, current]
    ret = []
    print("I got here 3")
    ret.append(process(fixed + [current], remaining[0], remaining[1:]))
    if current in ('1', '2') and len(remaining) != 1:
        print("I got here 1,2")
        ret.append(process(fixed+[current + remaining[0]], remaining[1], remaining[2:]))
    return ret

#Task 3.1

def task1(x, y):
   task3 = x*y+y
   print(task3)
   return task3

firstInt = int(input("Enter one number "))
secondInt = int(input("Enter another number number "))

task1(firstInt, secondInt)

#Task 3.2

firstNumber = int(input("Choose one number: "))
secondNumber = int(input("Choose another number: "))
firstOperator = input("What do you want to do with these numbers ")
if firstOperator == "+":
    print(firstNumber + secondNumber)
elif firstOperator == "-":
    print(firstNumber - secondNumber)
elif firstOperator == "/":
    print(firstNumber / secondNumber)
elif firstOperator == "*":
    print(firstNumber * secondNumber)
elif firstOperator == "//":
    print(firstNumber // secondNumber)
elif firstOperator == "%":
    print(firstNumber % secondNumber)
elif firstOperator == "**":
    print(firstNumber ** secondNumber)

#Task 3.4
#Spec = Special
#Char = Characters

Password = input("Write a sequence that is no longer than 8 characters and has at least 1 number in without å ä ö in ")

a = (Password[0])
a.isnumeric()
if len(Password) > 1:
    b = (Password[1])
    b.isnumeric()
if len(Password) > 2:
    c = (Password[2])
    c.isnumeric()
if len(Password) > 3:
    d = (Password[3])
    d.isnumeric()
if len(Password) > 4:
    e = (Password[4])
    e.isnumeric()
if len(Password) > 5:
    f = (Password[5])
    f.isnumeric()
if len(Password) > 6:
    g = (Password[6])
    g.isnumeric()
if len(Password) > 7:
    h = (Password[7])
    h.isnumeric()


def noSpecChar(Password):
    Numberlist = (0,1,2,3,4,5,6,7,8,9)
    Charlist = ("ä", "ö", "å")
    if len(Password) > 8:
        print("This is longer than 8 characters... failure ")
        return(Password)
    if Password == Password.count("å" or "ä" or "ö"):
        print("There is a character that is not allowed to be here... failure ")
        return(Password)
    if a or b or c or d or e or f or g or h == True:
        print("There is not a single number in here... failure ")
        return(Password)
    else:
        print("Thanks for entering a password you may continue... success ")

def noSpecChar1(Password):
    countAlph = Password.count('å') + Password.count('ä') + Password.count('ö')
    countnum = Password.count('0') + Password.count('1') + Password.count('2') + Password.count('3') + Password.count('4')
    countnum2 = Password.count('5') + Password.count('6') + Password.count('7') + Password.count('8') + Password.count('9')
    print(countAlph)
    print(countnum, countnum2)
    if len(Password) > 8:
        print("This is longer than 8 characters... failure ")
        return(Password)
    if countAlph > 0:
        print("There is a character that is not allowed to be here... failure ")
        return(Password)
    if countnum or countnum2 == 0:
        print("There is not a single number in here... failure ")
        return(Password)
    else:
        print("Thanks for entering a password you may continue... success ")

def noSpecChar2(Password):
    if len(Password) > 8:
        print("This is longer than 8 characters... failure ")
        return(Password)
    if ("å, ä, ö") in Password:
        print("There is a character that is not allowed to be here... failure ")
        return(Password)
    else:
        print("Thanks for entering a password you may continue... success ")
    if a != True or b != True or c != True or d != True or e != True or f != True or g != True or h != True:
        print("Why is there not a single number... failure")
        return(Password)

#noSpecChar(Password)
noSpecChar1(Password)
#noSpecChar2(Password)

#Task 4.1

word = input("input: ")
Numbers = sum(Number.isdigit() for Number in word)
Letters = sum(Letter.isalpha() for Letter in word)

print(Numbers, Letters)

#Task 4.2

numberOfTimes = int(input("hur många gånger ska den uppreppas"))
start = int(input("Lägg in ett start värde:"))
counting = 0
one = 1
if start == 1:
    print("0")
    print("1")
    print("1")
    counting = 3
if start == 2:
    print("1")
    print("1")
    counting = 2
if start == 3:
    print("1")
    counting = 1
if start <= 0:
    print("enter positiv number")
else:
    while counting < numberOfTimes:
        fibonacci = start + one
        one = start
        start = fibonacci
        counting += 1
        print(start)

#Task 7

elever = ['Axel', 'Johan', 'Johanna', 'Oscar', 'Bill']
elever2 = elever
tuple = tuple(elever2)
nummer = [1, 3, 4, 6, 2, 5]
elever.append("Joergen")
elever.append("Sven")
elever.sort() # I do not need to sort the students i one uses the sort funktion
nummer.sort(reverse=True)
if "Tom" in elever:
    print("tom är med i elver ")

basgrupp1 = elever[0], elever[1], elever[2]
basgrupp2 = elever[3], elever[4], elever[5], elever[6]
print(basgrupp1)
print(basgrupp2)
print(elever[0])
print(elever[2])
print(nummer)

tuple.sort()
elever2.sort()
print(tuple)
print(elever2)

#Skillnaden mellan en tuple och en list är att man kan förändra saker i en list men man kan inte förändra saker i en tuple








