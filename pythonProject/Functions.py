
num1 = input("Enter one number ")
num2 = input("Enter another number ")
num3 = input("Enter one more number ")


def numcheck():
    if num1 <= num2 and num1 <= num3:
        return num1

    elif num2 <= num1 and num2 <= num3:
        return num2

    elif num3 <= num1 and num3 <= num2:
        return num3

print(numcheck())



