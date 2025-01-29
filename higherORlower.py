
#import random

# def higher_or_lower():
#     print("Welcome to the Higher or Lower game!")
#     print("You start with a random number between 1 and 100.")
#     print("Guess if the next number will be higher or lower.")

#     current_number = random.randint(1, 100)
#     print(f"Starting number: {current_number}")

#     while True:
#         choice = input("Will the next numer be 'higher' or 'lower'? (or type 'exit' to quit): ").strip().lower()
#         if choice == "exit":
#             print("Thanks for playing!")
#             break

#         next_number = random.randint(1, 100)
#         print(f"The next number is: {next_number}")
#         if (choice == "higher" and next_number > current_number) or \
#            (choice == "lower" and next_number < current_number):
#             print("You guessed right!")
#         else:
#             print("You guessed wrong!")
#         current_number = next_number

#     if __name__ == "__main__":
#         higher_or_lower()

import random

def higher_or_lower():
    print("Welcome to the Higher or Lower game!")
    print("You start with a random number between 1 and 100.")
    print("Guess if the next number will be higher or lower.")

    current_number = random.randint(1, 100)
    print(f"Starting number: {current_number}")

    while True:
        choice = input("Will the next number be 'higher' or 'lower'? (or type 'exit' to quit): ").strip().lower()
        if choice == "exit":
            print("Thanks for playing!")
            break

        next_number = random.randint(1, 100)
        print(f"The next number is: {next_number}")
        if (choice == "higher" and next_number > current_number) or \
           (choice == "lower" and next_number < current_number):
            print("You guessed right!")
        else:
            print("You guessed wrong!")
        current_number = next_number

if __name__ == "__main__":
    higher_or_lower()