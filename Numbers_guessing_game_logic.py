import random
random_number = random.randint(1, 10)


def number_checker(num_input):
    high_or_low = None
    if num_input == random_number:
        return True
    else:
        if number_input > random_number:
            high_or_low = "high"
        else:
            high_or_low = "low"
        return f"Nope! Please, try again! Your number is too {high_or_low}. {tries_left} tries left."


tries_left = 3
while tries_left > 0:
    number_input = int(input("Pick a random number between 1 and 10: "))
    game_won = number_checker(number_input)

    if number_checker(number_input) == True:
        print(f"You guessed it! The random number was {random_number}.")
        break
    else:
        tries_left -= 1
        if tries_left == 0:
            print(f"You lost! The random number was {random_number}.")
        else:
            print(number_checker(number_input))

