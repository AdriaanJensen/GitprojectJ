character_name = ["Martin", "Lucas", "Adriaan"]
character_age = "46"
print("One day when " + character_name[0] + " was outside walking ")
print("one of his \"Friends\" " + character_name[1] + " came by and told him...")
print("Congrats, You`re " + character_age + " now")
print("and " + character_name[0] + " answered why must you bother me on this tragic day")
print("and the friend answered because it´s your birthday and that is a cause for celebration")
print("No thank you, " + character_name[0] + " answered ")
print(" ")
print(" ")
phrase = "Martin is real"
print(len(phrase))
for h in character_name:
    print("person " + h + ":")
print(" ")

# name = input("enter your name")
# age = input("enter your age")
# print("hello "+ name + " you are "+ age + " years old")

# print(" ")
# num1 = input("enter a number")
# num2 = input("enter another number")
# num3 = input("and yet another number")
# num4 = input("another")
# num5 = input("another")
# num6 = input("one last")
# result = int(num1) / int(num2) + int(num3) / int(num4) + int(num5) / int(num6)

# print(result)

# a = input("what is you name?")
# b = input("what is your sur name")
# print(a[:4]+b[-3:])
# import math
T_a = input("Numerator1")
N_a = input("Denominator1")
T_b = input("Numerator2")
N_b = input("Denominator2")
T_c = input("Numerator3")
N_c = input("Denominator3")

a1 = (float(T_a) * float(N_b))
c1 = (float(T_b) * float(N_a))
d1 = (float(N_b) * float(N_a))
e1 = (float(T_c) * float(d1))
f1 = (float(N_c) * float(d1))
a2 = (float(a1) * float(N_c))
c2 = (float(c1) * float(N_c))
ans = (float(a2)) * (float(c2)) * (float(e1))
#print(ans + "/" + f1)
