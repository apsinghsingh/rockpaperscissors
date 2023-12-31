import random
import time
score1 = 0
score2 = 0
while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    time.sleep(1)
    print("Rock")
    time.sleep(1)
    print("Paper")
    time.sleep(1)
    print("Scissors")
    time.sleep(1)
    print("Shoot")
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            score1 += 1
            print("Your score", score1, "AI score", score2)
            print("Rock smashes scissors! You win!")
        else:
            score2 += 1
            print("Your score", score1, "AI score", score2)
            print("Paper covers rock! You lose.")

    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            score1 += 1
            print("Your score", score1, "AI score", score2)
        else:
            score2 += 1
            print("Your score", score1, "AI score", score2)
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            score1 += 1
            print("Your score", score1, "AI score", score2)
            print("Scissors cuts paper! You win!")
        else:
            score2 += 1
            print("Your score", score1, "AI score", score2)
            print("Rock smashes scissors! You lose.")
    if score1 == 3:
        print("You win")
        break
    elif score2 == 3:
        print("You lost")
        break