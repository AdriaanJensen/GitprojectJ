
yes = "YES"
no = "NO"
is_male = input("Are you male? Yes or no?").upper()
if is_male == yes:
    is_male = True
else: is_male = False

is_tall = input("are you tall? Yes or no?").upper()
if is_tall == yes:
    is_tall = True
else: is_tall = False


if is_male and is_tall:
   print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male, but you are tall")
else:
   print("You are neither male nor tall ")

#def max_num(num1, num2, num3):
#    if num1 >= num2 and num1 >= num3:
#        return num1
#    elif num2 >= num1 and num2 >= num3:
#        return num2
#    else:
#        return num3
#print(max_num(300, 40, 5))
