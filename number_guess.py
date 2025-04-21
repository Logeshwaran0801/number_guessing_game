import random
def number_guessing_game():
    """
    This is a funny game where the computer guess one number we have to find the number within less attempts
    """
    computer_guess=random.randint(1,100)
    attempts=0
    print("WELCOME TO NUMBER GUESSING NAME")
    print("Iam  thinking a number...")
    while True:
        user_guess=input("your guess:")
        if user_guess.lower()=="quit":
            print("Wanna Give up Lol")
            break
        
        try:
            user_guess=int(user_guess)
        except ValueError:
           print("please provide numbers only")
           continue

        if user_guess<1 or user_guess>100:
            print("please provide the numbers from(1-100)")
            continue
        attempts+=1

        if user_guess==computer_guess:
            print("you are correct!")
            print(f"congratulations you have find the number with {attempts} attempts")
        
        elif user_guess<computer_guess:
            print("Too low! Try again")
        else:
            print("Too High !Try again")
number_guessing_game()
    
    
    
     
