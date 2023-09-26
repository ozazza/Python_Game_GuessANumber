import random

computer_number = random.randint(1, 100)

# Read Player's Move
while True:
    steps_max = 6
    steps_counter = 0
    is_guessed = False

    while steps_counter < steps_max:
        player_input = input('Guess the number (1-100): ')

        steps_counter += 1
        steps_left = steps_max-steps_counter

        if not player_input.isdigit():
            print('Invalid input. Try again...')
            continue
        else:
            player_number = int(player_input)

            if player_number == computer_number:
                print('You guess it!')
                is_guessed = True
                break
            elif player_number < computer_number:
                print('Too low!')
            elif player_number > computer_number:
                print('Too high!')

        # Show difficulty
        print(f'< Steps left {steps_left} >')

    if is_guessed:
        print('<<< ------------(O)------------>>>')
        print('<<< Victory! You won the game! >>>')
    else:
        print(f'Sorry! The number was <<< {computer_number} >>>. Try another game!')

    # Ask to play again
    ask_player = input('Play again? (y / n): ')
    if ask_player == 'y':
        pass
    else:
        print('Okay, bye!')
        break

