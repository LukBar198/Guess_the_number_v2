from random import randint


def guess_number():
    """Guess the number the GAME v2 - without decorator

    :return:
    """
    computer_number = randint(1, 100)

    while True:
        try:
            player_number = float(input("Guess the number: "))
        except (ValueError, TypeError):
            print("It's not a number!")
            continue

        if computer_number is player_number:
            print("You win!")
            break
        elif computer_number < player_number:
            print("Too big!")
        elif computer_number > player_number:
            print("Too small!")


guess_number()
