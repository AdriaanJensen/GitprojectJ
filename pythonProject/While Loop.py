
#While Loops
Question = int(input("Task? "))

while Question == 1:
    secret_word = "hello"
    guess = ""
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False

    while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter guess")
            guess_count += 1
        else:
            out_of_guesses = True

    if out_of_guesses:
        print("Out of guesses you lose")
        Question = int(input("New task? "))
    else:
        print("You succeed")
        Question = int(input("New task? "))

# Task 1

while Question == 2:
    Number = 0
    while Number <= 20:
        print(Number)
        Number += 2
    Question = int(input("New task? "))

# Task 2

while Question == 3:
    tak = 100
    Summa = 0
    print("Make it 100, one number at a time ")
    while Summa < tak:
        n = int(input(""))
        Summa += n
        print("The sum total is " + str(Summa))
    print("Thank you")
    Question = int(input(" New task? "))

# Task 3

while Question == 4:
    Dum_Question = str.lower(input("Do you want to play a game? "))
    while Dum_Question == "yes":
        Dum_Question = str.lower(input("Do you want to play a game again? "))
    if Dum_Question == "no":
        print("I don't want to play with you either")
        print(" ")
        Question = int(input("New task? "))

# Task 4

while Question == 5:
    import random
    Max_number = 100
    Good_number = random.randrange(Max_number)
    Guess = int(input("Guess the number"))
    number_of_Guesses = 0
    while Guess != Good_number:
        if Guess < Good_number:
            print("Higher")
            Guess = int(input("Guess again: "))
            number_of_Guesses += 1
        elif Guess > Good_number:
            print("Lower")
            Guess = int(input("Guess again: "))
            number_of_Guesses += 1
        if Guess == Good_number:
            print("You win")
            Question = int(input("New Task? "))
        if number_of_Guesses == 10:
            print("Game over")
            Question = int(input("New Task? "))
