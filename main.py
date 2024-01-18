import random
def game_round(playerChoice, computerChoice):
    if playerChoice == computerChoice:
        return 0
        #it's a tie
    elif ( playerChoice == "rock" and computerChoice == "scissors" ) or ( playerChoice == "scissors" and computerChoice == "paper" ) or ( playerChoice == "paper" and computerChoice == "rock"):
        return  1
        #player wins
    else:
        return -1
        #computer wins

#main code
def main():
    # initialising player and computer score
    playerScore = 0
    computerScore = 0

    # creating a loop for number of rounds(which is 3)
    for i in range(1, 4):
        print(f'Round {i}')
        print('1.Rock 2.Paper 3.Scissors')

        choiceNum = int(input('Enter your choice number: '))
        if choiceNum > 3 or choiceNum < 1:
            print('Invalid choice, please enter a number between 1 and 3')
            main()
            #loops back to main function

        # create an array of choices
        choiceElements = ['rock', 'paper', 'scissors']
        playerChoice = choiceElements[choiceNum - 1]
        print(f'You chose: {playerChoice}')
        computerChoice = random.choice(choiceElements)
        print(f'computer chose: {computerChoice}')

        # Determine the winner of the round
        result = game_round(playerChoice, computerChoice)
        if result == 1:
            print('You win this round!')
            playerScore += 1
        elif result == -1:
            print('Computer wins this round!')
            computerScore += 1
        else:
            print('It\'s a tie!')

    # Determine the final winner
    print('Game Over!')
    print(f'Your score: {playerScore}')
    print(f'Computer\'s score {computerScore}')
    print('\n ')
    if playerScore > computerScore:
        print('Congratulations! you won!')
    elif playerScore < computerScore:
        print('oops! better luck next time')
    else:
        print('The game ends in a tie')

    #asking the user if they want to play again
    ans = input('Do you wanna play again? y or n ')
    if ans == 'y':
        main()
    else:
        print('Thanks for playing!')

if __name__ == "__main__":
    main()
