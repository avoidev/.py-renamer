import random

number_gen = random.randint(1, 10)

randomnumber = str(number_gen)
lives = 3
thesecretstring = "potato"

print("You have to guess the random number between 1 and 10!")
print("You currently have " + str(lives) + " out of 3 lives left!")

print("           -------------")
print("          | Answer is " + randomnumber + " |")
print("           -------------")

guess = input("What is your guess?")

while lives != 0 and guess != randomnumber:
    lives = lives - 1
    if guess != randomnumber:
        if guess >= "11" or guess <= "0":
            print("Can you not read?? The question states that the number is between 1 and 10...")
            print("")
        if guess == thesecretstring:
            print("A Secret!")
            break
        if guess == "reset":
            print("shhh... setting lives to 3 again.")
            lives = 3

        print("Your guess was wrong! You now only have " + str(lives) + " lives left!")
        guess = input("What is your guess?")

    elif guess == randomnumber:
        break

if guess == randomnumber:
    print("Congrats, you guessed correctly!")

if guess == thesecretstring:
    print("Well aren't you cleaver....")

if lives == 1:
    print("You ran out of lives!")
