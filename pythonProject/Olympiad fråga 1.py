
#Task 1

Tortimetoeat = int(input("Write one number between 1-100: "))
Mothertimetoeat = int(input("Write one number between 1-100: "))
Carrots = 40
Seconds = 0
Nextsecondfortor = 1
Nextsecondformother = 1
Torcarrotcount = 0
Mothercarrotcount = 0

while Carrots > 0:
    if Carrots == 1 and Nextsecondfortor == Nextsecondformother:
        break
    if Seconds == Nextsecondfortor:
        Carrots -= 1
        Nextsecondfortor += Tortimetoeat
        Torcarrotcount += 1
    if Seconds == Nextsecondformother:
        Carrots -= 1
        Nextsecondformother += Mothertimetoeat
        Mothercarrotcount += 1
    Seconds += 1

print("The amount of carrots Tor ate is:", Torcarrotcount)
print("The amount of carrots Tors mother ate is:", Mothercarrotcount)
print("The amount of seconds to eat everything:", Seconds)

#Task 2

#Clumpofnumbers = input("Write a clump of numbers(Maximum of 15 digits): ")
Clumpofnumbers = "2312410"
#Clumpofnumbers = "112"
Clumpofnumbersoriginallist = list(Clumpofnumbers)
Clumpofnumbersworkinglist = Clumpofnumbersoriginallist
Lengthoflist = len(Clumpofnumbersoriginallist)
TheIndex = 0
Alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ")

def process2(fixed, current, remaining):
    if len(remaining) == 0:
        print("I got here 1")
        return [fixed, current]
    ret = []
    print("I got here 3")
    ret.append(process2(fixed + [current], remaining[0], remaining[1:]))
    if current in ('1', '2') and len(remaining) != 1:
        print("I got here 1,2")
        ret.append(process2(fixed+[current + remaining[0]], remaining[1], remaining[2:]))
    return ret

def neighbors(node):
  if node.current in ('1', '2'):
    return [node.current, node.current*10 + node.next]
  return [node.current]

remaining = Clumpofnumbers

print(process2([], "3", Clumpofnumbersoriginallist))
Cipherlist = process2([], "3", Clumpofnumbersoriginallist)
#print(len(process2([], "0", Clumpofnumbersoriginallist)))
print(len(Cipherlist))
