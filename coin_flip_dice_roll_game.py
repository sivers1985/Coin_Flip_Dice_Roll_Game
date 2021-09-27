import random

def guess_coin_flip():
    guess = input("Enter h for heads, t for tails or 0 to return to main menu: ")
    print(guess)
    correct = 0
    total = 0
    while True:
        coin_flip = random.randint(0, 1)
        if guess == "0":
            break
        elif (coin_flip == 0 and guess == "h"):
            print("The coin flip was heads.")
            print("You guessed correct!")
            correct += 1
            total += 1
            print("Your win percentage is " + str(round(correct/total * 100)) + "%")
        elif (coin_flip == 1 and guess == "t"):
            print("The coin flip was tails.")
            print("You guessed correct!")
            correct += 1
            total += 1
            print("Your win percentage is " + str(round(correct/total * 100)) + "%")
        elif (coin_flip == 0 and guess == "t"):
            print("The coin flip was heads.")
            print("Your guess was incorrect.")
            total += 1
            print("Your win percentage is " + str(round(correct/total * 100)) + "%")
        elif (coin_flip == 1 and guess == 'h'):
            print("The coin flip was tails.")
            print("You're guess was incorrect")
            total += 1
            print("Your win percentage is " + str(round(correct/total * 100)) + "%")
        else:
            print("Please enter a valid guess.")
        guess = input("Enter h for heads, t for tails or 0 to return to main menu: ")
        print(guess)

def guess_dice_roll():
    guess = int(input("Enter a guess for a six-sided die or 0 to return to main menu: "))
    print(guess)
    correct = 0
    total = 0
    while True:
        roll = random.choice([x for x in range(1, 7)])
        if guess == 0:
            break
        elif guess == roll:
            correct += 1
            total += 1
            print("You guessed " + str(roll) + ", that was correct!")
            print("Your win percentage is " + str(round(correct/total * 100)) + "%")
        elif (guess != roll) and (guess in range(1, 7)):
            total += 1
            print("You guessed " + str(guess) + ", the roll was " + str(roll) + ", that was incorrect.")
            print("Your win percentage is " + str(round(correct/total * 100)) + "%")
        else:
            print("Please enter a valid guess.")
        guess = int(input("Enter a guess for a six-sided die or 0 to return to main menu: "))
        print(guess)

def run_game():
    choice = input("Enter 1 for coin flip game, 2 to roll a die or 0 to exit: ")
    print(choice)
    while True:
        if choice == "0":
            break
        elif choice == "1":
            guess_coin_flip()
        elif choice == "2":
            guess_dice_roll()
        else:
            print("Please enter a valid choice")
        choice = input("Enter 1 for coin flip game, 2 to roll a die or 0 to exit: ")
        print(choice)

run_game()