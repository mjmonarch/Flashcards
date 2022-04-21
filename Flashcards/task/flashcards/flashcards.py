# ------------------------------------------STAGE 1------------------------------------------
# print("Card:")
# print('A. Einstein')
# print('Definition:')
# print('German-born theoretical physicist,[7] widely acknowledged to be one of the greatest '
#       'and most influential physicists of all time. ')

# ------------------------------------------STAGE 2------------------------------------------
# card = input()
# definition = input()
# answer = input()
#
# if definition == answer:
#       print("Your answer is right!")
# else:
#       print("Your answer is wrong...")


# ------------------------------------------STAGE 3------------------------------------------
# num = int(input("Input the number of cards:\n"))
#
# flashcards = {}
# for i in range(num):
#     term = input(f"The term for card #{i + 1}:\n")
#     definition = input(f"The definition for card #{i + 1}:\n")
#     flashcards[term] = definition
#
# for key, value in flashcards.items():
#     answer = input(f"Print the definition of \"{key}\":\n")
#     if answer != value:
#         print(f"Wrong. The right answer is \"{value}\".")
#     else:
#         print("Correct!")

# ------------------------------------------STAGE 4------------------------------------------
# num = int(input("Input the number of cards:\n"))
#
# flashcards = {}
# for i in range(num):
#     term = input(f"The term for card #{i + 1}:\n")
#     while True:
#         if term not in flashcards.keys():
#             break
#         else:
#             term = input(f"The term \"{term}\" already exists. Try again:\n")
#     definition = input(f"The definition for card #{i + 1}:\n")
#     while True:
#         if definition not in flashcards.values():
#             break
#         else:
#             definition = input(f"The definition \"{definition}\" already exists. Try again:\n")
#     flashcards[term] = definition
#
# for key, value in flashcards.items():
#     answer = input(f"Print the definition of \"{key}\":\n")
#     if answer == value:
#         print("Correct!")
#     elif answer in flashcards.values():
#         print(f"Wrong. The right answer is \"{value}\", but your definition is correct for "
#               f"{list(flashcards.keys())[list(flashcards.values()).index(answer)]}")
#     else:
#         print(f"Wrong. The right answer is \"{value}\".")

# ------------------------------------------STAGE 5------------------------------------------
from pathlib import Path
import json
import random

flashcards = {}

while True:
    choice = input("Input the action (add, remove, import, export, ask, exit):\n")
    if choice == 'add':
        term = input("The card:\n")
        while True:
            if term not in flashcards.keys():
                break
            else:
                term = input(f"The card \"{term}\" already exists. Try again:\n")
        definition = input("The definition of the card:\n")
        while True:
            if definition not in flashcards.values():
                break
            else:
                definition = input(f"The definition \"{definition}\" already exists. Try again:\n")
        flashcards[term] = definition
        print(f"The pair (\"{term}\":\"{definition}\") has been added.\n")
    elif choice == 'remove':
        card = input("Which card?\n")
        if card in flashcards.keys():
            flashcards.__delitem__(card)
            print("The card has been removed.")
        else:
            print(f"Can't remove \"{card}\": there is no such card.")
        print()
    elif choice == 'import':
        file_name = input("File name:\n")
        if Path(file_name).is_file():
            with open(file_name, 'r') as json_file:
                inp_dict = json.load(json_file)
            i = 0
            for key, value in inp_dict.items():
                flashcards[key] = value
                i += 1
            print(f"{i} cards have been loaded.")
        else:
            print("File not found.")
        print()
    elif choice == 'export':
        file_name = input("File name:\n")
        with open(file_name, "w") as json_file:
            json.dump(flashcards, json_file)
        print(f"{len(flashcards)} cards have been saved.\n")
    elif choice == 'ask':
        q = int(input("How many times to ask?\n"))
        for i in range(q):
            card = random.choice(list(flashcards.keys()))
            answer = input(f"Print the definition of \"{card}\":\n")
            if answer == flashcards[card]:
                print("Correct!")
            elif answer in flashcards.values():
                print(f"Wrong. The right answer is \"{flashcards[card]}\", but your definition is correct for \""
                      f"{list(flashcards.keys())[list(flashcards.values()).index(answer)]}\".")
            else:
                print(f"Wrong. The right answer is \"{flashcards[card]}\".")
    elif choice == 'exit':
        print("Bye bye!")
        break
    else:
        print("Incorrect option. Try again!")
