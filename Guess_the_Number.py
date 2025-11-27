import random

def jugar():
    print("Guess the number (from 1 to 100), you have 7 attempts.")

    # Randomly generated secret number
    secreto = random.randint(1, 100)

    # Attempt counter starts at 0
    intentos = 0

    while True:
        try:
            # Ask the user for a number
            texto = input("Enter a number: ")
            u = int(texto)  # Converts input to int; avoids failure if it's not a number

        except ValueError:
            # If input is not a valid number, this prevents the code from crashing
            print("Invalid number, please try again.")
            continue  # Allows the code to continue if the value is not a number

        # Valid number received, increase the counter
        intentos += 1

        # Compare user number with the secret number
        if u > secreto:
            print("Lower...")
        elif u < secreto:
            print("Higher...")
        else:
            print(f"Correct! The secret number was {secreto}. You guessed it in {intentos} attempts.")
            break

        # If attempts are finished
        if intentos == 7:
            print(f"GAME OVER. The secret number was {secreto}.")
            break

# Main loop to repeat rounds and start the game again
while True:
    jugar()
    op = input("Do you want to play again? (y/n): ").lower()
    if op == "n":
        print("Thanks for playing!")
        break
