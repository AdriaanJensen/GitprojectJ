
# Task 1

List1 = ["Kevin", "Karen", "Jim", "Jim", "Martin"]
print(List1)
List2 = List1.copy()
List2.reverse()
print(List2)
element1 = List2.pop(0)
print(element1)
List1.insert(2, element1)
print(List1)
print(List1.count(element1))
print(" ")
print(" ")

# Task 2  1+2


Numbers1 = [33, 11, 56, 29, 65]
Numbers1.append(47)
print(Numbers1)
Numbers2 = Numbers1.copy()
Numbers2.reverse()
Numbers2.extend(Numbers1)
print(Numbers2)
print(" ")
print(" ")
# Append adds an element to it while Extend adds elements of an already existing list.


# Task 2  3


Numbers1.pop(2)
print(Numbers1)
Numbers2.remove(65)
print(Numbers2)
print(" ")
print(" ")
# Pop removes a specific position regardless of number while Remove takes away a specific number regardless of position.


# Task 2  4

Numbers2.sort()
print(Numbers2)
print(" ")

Number_of_elements = len(Numbers2)
print("Number of elements in the list: ", Number_of_elements)
print(" ")

l = Numbers2
count = 0
for i in l:
    count = count + 1
print("The length of the list is", count)





















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































