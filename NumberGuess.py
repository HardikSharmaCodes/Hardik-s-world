import random

Player_Guess = int(input("Write Your Number: ")) 

random_number = random.randint(1, 1000000)

def guess():    
    if Player_Guess >= random_number - 100 and Player_Guess< random_number:
        print(f"Your guess {Player_Guess} is close, try adding a little bit more to it.")
    elif Player_Guess <= random_number + 100 and Player_Guess > random_number:
        print(f"Your guess {Player_Guess} is close, try subtracting a little bit off to it.")
    elif Player_Guess > random_number:
        print(f"Your guess is {Player_Guess} is wrong, subtract.")
    elif Player_Guess < random_number:
        print(f"Your guess is {Player_Guess} is wrong, add.")
    else:
        print("invalid number")

for i in range(1, 100000000000000000000000000000):
    if Player_Guess == random_number:
        print(f"You guessed the right number: {random_number}")
        break
    else: 
        guess()
        Player_Guess = int(input("Write Your Number: ")) 



