# This program is to emulate a guessing game using break/continue and for loops
import random


rand_number = random.randint(1,100) # Random number
quit = False # Flag to quit from loop
correct = False # Flag to announce result after loop

print("Eneter a number between 1-100\n")

for chance in range(7, 0, -1): # Loop iteration in reverse(-ve)
    print(f"You have {chance} chances remaining!")

    while True:
        number = input("Enter a number or 'quit' to exit: ") # User input
        
        # checks if input is a number then convert to int
        if number.lstrip('-+').isdigit():       # .lstrip('-+') to cound -ve number (number with sign)
            number = int(number)
            if number > 100 or number < 0:
                print("ENTER between 1-100!")
                continue
            break
        
        elif number.lower() == "quit":  # checks if user wants to quit
            quit = True
            break
            
        else:
            print("Enter a NUMBER!")
            continue

    # breaks out from loop if True
    if quit:
        print(f"The Number was {rand_number}!")
        break
    
    # Checks and compare input and rand_num
    if number == rand_number:
        print(f"You have guessed the correct number! -> {rand_number} <-")
        correct = True
        break

    # Gives the player a chance to guess the correct answer
    else:
        if abs(number - rand_number) < 5:   # abs() to get +ve value from subtractions
            print("Very Very close!")
            continue

        if abs(number - rand_number) < 15:
            print("Very close!")
            continue
        
        if number > (rand_number + 25): 
            print("Too HIGH!")
            continue

        if number < (rand_number - 25): 
            print("Too LOW!")
            continue

if not correct:
    print(f"\n--------The Number was {rand_number}!--------")

            

