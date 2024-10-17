import random

def game():
    print("Welcome to Rock-Paper-Scissors!")
    #initialize score counter
    player_wins = 0
    computer_wins = 0
    total_games = 0
    tie = 0
    
    while True:
        user_choice = input("Enter your choice: rock, paper, scissors or 'exit': ").lower()

        if user_choice == 'exit':
            break
        #validate user input
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice, please try again.")
            continue
        #randomly select the computer's choice
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print("Computer chose:", computer_choice)
        #increment total games counter
        total_games += 1
        #to determine the outcoe of the game
        if user_choice == computer_choice:
            print("It's a tie!")
            tie +=1 #increment tie counter
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
            player_wins += 1 #increment player wins
        else:
            print("You lose!")
            computer_wins += 1 #increment computer wins

        print(f"Scores:\nPlayer Wins: {player_wins}\nComputer Wins: {computer_wins}\nTies: {tie}\nTotal Games: {total_games}\n")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Final Scores:")
    print(f"Player Wins: {player_wins}\nComputer Wins: {computer_wins}\nTies: {tie}\nTotal Games: {total_games}")

game()