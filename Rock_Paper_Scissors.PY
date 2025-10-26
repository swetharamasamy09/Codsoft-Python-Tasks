import random

def play_game():
    print("Welcome to Rock_Paper_Scissors game")
    choice=["rock","paper","scissors"]

    while True:
        user_choice=input("Enter your choice (rock/paper/scissors or quit):")

        if user_choice=="quit":
            print("Thanks for playing !!")
            break

        if user_choice not in choice:
            print("Invalid choice !please choose rock,paper,or scissors.")
            continue

        computer_choice=random.choice(choice)
        print(f"\nYou chose:{user_choice}")
        print(f"computer chose:{computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")

        elif(user_choice =="rock"and computer_choice=="scissors")or\
            (user_choice =="paper"and computer_choice=="rock")or\
            (user_choice =="scissors"and computer_choice=="paper"):
            print("YOU wIN")
        
        else:
            print("oops! You Lose...")

        print("_"*30)
        
play_game()