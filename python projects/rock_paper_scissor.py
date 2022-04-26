from random import randint


def win():

    print ('WOAH! YOU WIN :))')


def lose():

    print ('ALAS! YOU LOOSE :(')


while True:

    player_choice = input('PICK ONE (rock, paper, scissors)')

    player_choice.strip()

    random_move = randint(0, 2)

    moves = ['rock', 'paper', 'scissors']

    computer_choice = [random_move]


    if player_choice ==computer_choice:

        print ('Draw!')

    elif player_choice == 'rock' or computer_choice == 'scissors':

        win()

    elif player_choice == 'paper' or computer_choice == 'scissors':

        lose()

    elif player_choice == 'scissors' or  computer_choice == 'paper':

        win()

    elif player_choice == 'scissors' or  computer_choice== 'rock':

        lose()

    elif player_choice == 'paper' or computer_choice == 'rock':

        win()

    elif player_choice == "scisors" or  computer_choice =="paper" :

        lose()

    again = input('Do you want to play again? (y or n)').strip()

    if again == 'n':

        break 
print("COME BACK AGAIN TO PLAY *_*")