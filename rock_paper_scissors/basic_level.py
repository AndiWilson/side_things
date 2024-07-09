# Welcome to my beginner level rock, paper, scissors game.... just for funsies >.<
import random
num = [1, 2, 3]
print("Welcome to Rock, Paper, Scissors!\n")

# takes user input
user = input("Please... tell me your name: \n")
print("Nice to meet you, " + user + "\n")

# introduce computer
print("Your opponent is Dave")
print("Dave is very good...\n")

choices = {"rock": 1, "paper": 2, "scissors": 3}

# iterate through 10 games
i = 0
tied_games = 0
user_wins = 0
computer_wins = 0

while i < 10:
    computer_choice = random.choice(num)

    # user choice
    user_choice = input("Please choose between rock, paper, and scissors: ") 
    if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
        print("Your choice: " + user_choice)
    else:
        print("Invalid input! Please choose 'rock', 'paper', or 'scissors'")

    # computer choice
    if computer_choice == 1:
        computer_choice = "rock"
    elif computer_choice == 2:
        computer_choice = "paper"
    else:
        computer_choice = "scissors"
    print("Dave has chosen: " + computer_choice)

    #determine winner
    if user_choice == computer_choice:
        tied_games += 1
        print("It's a tie!\n")
    elif user_choice == "rock" and computer_choice == "paper":
        computer_wins += 1
        print ("Dave Wins!\n")
    elif user_choice == "rock" and computer_choice == "scissors":
        user_wins += 1
        print ("You Win!\n")
    elif user_choice == "paper" and computer_choice == "rock":
        user_wins += 1
        print ("You Win!\n")
    elif user_choice == "paper" and computer_choice == "scissors":
        computer_wins += 1
        print ("Dave Wins!\n")
    elif user_choice == "scissors" and computer_choice == "rock":
        computer_wins += 1
        print ("Dave Wins!\n")
    else:
        user_wins += 1
        print ("You Win!\n")

    # add an iteration
    i = i + 1

print("Tied games: ", tied_games)
print("You won: ", user_wins)
print("Dave won: ", computer_wins)
print("Good Game!")