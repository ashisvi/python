import random

""" Guess the number game """

start = 1
end = 50


def play(start=1, end=50):
    random_num = random.randint(start, end)
    lives = 10

    print(f"Guess the number between {start} to {end}:", end=" ")
    while lives > 0:
        lives = lives - 1
        _input = int(input())

        if lives <= 0:
            print("You lost")
            break

        if random_num == _input:
            print("You won")
            break
        elif random_num > _input:
            print("Too low, guess again:", end=" ")
        else:
            print("Too big, guess again:", end=" ")

    while True:
        playAgain = input("Do you want to play again (Y/N) : ")
        match playAgain:
            case 'y' | 'Y':
                play()
            case 'n' | 'N':
                exit()
            case _:
                print("Invalid response")


play()
