Strings = input("Write any word here")
print("there are", len(Strings), "signs in the word", Strings)
print("the first three letters in the word", Strings, "are", Strings[0:3])
try:
    print("The first A to appear in the word", Strings, "is in position", Strings.index("a") + 1)
except ValueError:
    print("There exists no letter A in the word", Strings, )
if Strings.islower(): print("The word", Strings, "only has lowercase letters")
if not Strings.islower(): print(Strings, "is not only in lowercase letters")

Mening = input("Write a sentence:")
print("The sentence has", len(Mening.split()), "words in it.")
print("The last a in the sentence is in position", Mening.rfind("a"))
print("Does the sentence end in a period?", Mening.endswith("."))
Mening = Mening.title()
Mening = Mening.swapcase()
print(Mening)










