import random

computer_number = random.randint(1, 100)

# Read Player's Move
steps_max = 6
steps_counter = 0
is_guessed = False

# Show difficulty
print(f'')
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
    print('<<< Victory! You won the game! >>>')
else:
    print('Sorry! Try another game!')

    print(f'steps: {steps_counter}')
