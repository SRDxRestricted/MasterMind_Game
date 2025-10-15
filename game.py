import random

Colors = ["R", "B", "W", "Y", "G", "O"]
Tries = 10
Code_length = 4

def generate_code():
    code = []

    for _ in range(Code_length):
        color = random.choice(Colors)
        code.append(color)

    return code

def guess_code():

    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != Code_length:
            print(f"You must guess {Code_length} colors.")
            continue

        for color in guess:
            if color not in Colors:
                print(f"Invalid Color {color} Try again.")
                break
        else:
            break

    return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1
    
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to Masterminid... You have {Tries} tries to guess the code")
    print("The valid colors are ", *Colors)

    code = generate_code()
    for attempts in range(1, Tries +1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == Code_length:
            print(f"You guessed the code in {attempts} tries!")
            break

        print(f"Correct Positions: {correct_pos} | Incorrect Position: {incorrect_pos}")

    else:
        print("You ran out of tries,  the code was: "*code)

if __name__ ==  "__main__":
    game()

