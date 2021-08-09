import random

random_number = random.randint(1,9)
tries = 1
 
question = input("Would you Like To Play A Game? [y/n] ")
 
if question == "n":
    print("oh..okay :(")
 
if question == "y":
    print("I'm Thinking Of A Number Between 1 & 9")
    guess = int(input("Have a Guess :"))
    if guess > random_number:
        print("Guess Lower...")

    if guess < random_number:
        print("Guess Higher...")
 
    while guess != random_number:
        tries += 1
        if(tries == 6):
            print("It took you more than 5 attempts! You lose. The real number was " + str(random_number))
            break
        guess = int(input("Try Again : "))
        if guess <random_number:
            print("Guess Higher...")
    if guess == random_number:
        print("You're Right! you win! The Number Was ", random_number, "and it only took ", tries, "tries!")
 