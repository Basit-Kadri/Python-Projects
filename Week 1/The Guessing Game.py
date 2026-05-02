import random


num = random.randint(0, 100)

print("This game involves the system printing a random number between 0 and 100. Your job is to guess the number"
                      "and if you guess wrong, the system will tell you whether your guess is high or low."
                      "If the guess is off by 10 numbers, it will say a little high/low, if it is off by 25 numbers, it"
                      "will say high or low and if it is off by 50 numbers, it will say too high/low...Ready?")
tries = 0
while True:
    tries += 1
    userguess = int(input("Please enter your guess: "))

    if userguess > num and userguess - num <= 10:
        print("The number you have input is a little high, your guess is greater than the number")
    elif userguess > num and userguess - num >= 11 and userguess - num <= 25:
        print("The number you have input is high, your guess is greater than the number")
    elif userguess > num and userguess - num >= 26 and userguess - num <= 50:
        print("The number you have input is too high, your guess is greater than the number")
    elif userguess == num:
        print(f"Congratulations! You've guessed the right answer in {tries} tries!")
        break

    elif userguess < num and num - userguess <= 10:
        print("The number you have input is a little low, your guess is lesser than the number")
    elif userguess < num and num - userguess >= 11 and num - userguess <= 25:
        print("The number you have input is low, your guess is lesser than the number")
    elif userguess < num and num - userguess >= 26 and num - userguess <= 50:
        print("The number you have input is too low, your guess is lesser than the number")




