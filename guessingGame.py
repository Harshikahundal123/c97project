import random 
print("Number Guessing Game")
number = random.randint(1,9)
print(number)
chances = 0 
print("Guess a number between 1 and 9 ")
while chances <5 :
    guess = int(input("Enter your input:"))
    if guess == number:
        print("Congratulation YOU WON!!")
        break
    elif guess <number : 
        print ( "Your guess is too low! Try again",guess)
    elif guess>number :
        print("Your guess is too high, try again!", guess)
    chances+=1 
if not chances < 5 :
        print ("You LOSE!!! The number is", number)

    