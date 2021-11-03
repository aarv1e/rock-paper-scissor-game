import random

CHOICES = ["rock","paper","scissor"]           #the list of valid choices
def gameWin (comp , you):                      #creating a method to determine the winner between comp and user
    if comp == you:
        print("The game is a draw")
    elif comp == "scissor":
        if you == "paper":
            print("The computer won")
        elif you == "rock":
            print("You won")
    elif comp == "paper":
        if you == "scissor":
            print("You won")
        elif you == "rock":
            print("The computer won")
    elif comp == "rock":
        if you == "paper":
            print("You won")
        elif you == "scissor":
            print("The computer won")

while True:                                                                           #initialising an endless loop 
    print("Make your throw")
    user_choice = input("Type rock, paper or scissor: ")
    if user_choice.lower() in CHOICES:
        computer_choice = random.choice(CHOICES)                                      #using the 'choice' method of the 'random' module to determine the comp choice
        print(f"You threw '{user_choice}', the computer threw '{computer_choice}'")
    else:
        print(f"{user_choice} isn't a valid throw")

    gameWin(computer_choice,user_choice.lower())                                      #calling the 'gameWin' function to determine the winner amongst comp and user

    again = input("Want to play again? (y/n): ")                                      #asking the user whether he wants to continue the game
    if again.lower() == "n":
        break

    print()

print("Goodbye")
