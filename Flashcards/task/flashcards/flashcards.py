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

# # ------------------------------------------STAGE 5------------------------------------------
# from pathlib import Path
# import json
# import random
#
# flashcards = {}
#
# while True:
#     choice = input("Input the action (add, remove, import, export, ask, exit):\n")
#     if choice == 'add':
#         term = input("The card:\n")
#         while True:
#             if term not in flashcards.keys():
#                 break
#             else:
#                 term = input(f"The card \"{term}\" already exists. Try again:\n")
#         definition = input("The definition of the card:\n")
#         while True:
#             if definition not in flashcards.values():
#                 break
#             else:
#                 definition = input(f"The definition \"{definition}\" already exists. Try again:\n")
#         flashcards[term] = definition
#         print(f"The pair (\"{term}\":\"{definition}\") has been added.\n")
#     elif choice == 'remove':
#         card = input("Which card?\n")
#         if card in flashcards.keys():
#             flashcards.__delitem__(card)
#             print("The card has been removed.")
#         else:
#             print(f"Can't remove \"{card}\": there is no such card.")
#         print()
#     elif choice == 'import':
#         file_name = input("File name:\n")
#         if Path(file_name).is_file():
#             with open(file_name, 'r') as json_file:
#                 inp_dict = json.load(json_file)
#             i = 0
#             for key, value in inp_dict.items():
#                 flashcards[key] = value
#                 i += 1
#             print(f"{i} cards have been loaded.")
#         else:
#             print("File not found.")
#         print()
#     elif choice == 'export':
#         file_name = input("File name:\n")
#         with open(file_name, "w") as json_file:
#             json.dump(flashcards, json_file)
#         print(f"{len(flashcards)} cards have been saved.\n")
#     elif choice == 'ask':
#         q = int(input("How many times to ask?\n"))
#         for i in range(q):
#             card = random.choice(list(flashcards.keys()))
#             answer = input(f"Print the definition of \"{card}\":\n")
#             if answer == flashcards[card]:
#                 print("Correct!")
#             elif answer in flashcards.values():
#                 print(f"Wrong. The right answer is \"{flashcards[card]}\", but your definition is correct for \""
#                       f"{list(flashcards.keys())[list(flashcards.values()).index(answer)]}\".")
#             else:
#                 print(f"Wrong. The right answer is \"{flashcards[card]}\".")
#     elif choice == 'exit':
#         print("Bye bye!")
#         break
#     else:
#         print("Incorrect option. Try again!")

# ------------------------------------------STAGE 6------------------------------------------
from pathlib import Path
import json
import random
import logging
import sys
import shutil


class Flashcard:

    def __init__(self, term, definition, mistakes=0):
        self.term = term
        self.definition = definition
        self.mistakes = int(mistakes)

    def reset(self):
        self.mistakes = 0

    def add_mistake(self):
        self.mistakes += 1

    @staticmethod
    def to_dictionary(flashcards_list: list) -> dict:
        return {flashcard.term: [flashcard.definition, flashcard.mistakes] for flashcard in flashcards_list}

    @staticmethod
    def from_dictionary(flashcards_dict: dict) -> list:
        return [Flashcard(key, value[0], value[1]) for key, value in flashcards_dict.items()]

    @staticmethod
    def get_flashcard(flashcards_list: list, term: str):
        for flashcard in flashcards_list:
            if flashcard.term == term:
                return flashcard
        return None


flashcards = []
logging.basicConfig(handlers=[logging.FileHandler('temp_log_file.log'), logging.StreamHandler(sys.stdout)],
                    format='%(message)s', level='DEBUG')


while True:
    logging.info("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):")
    choice = input()

    if choice == 'add':
        logging.info("The card:")
        term = input()
        while True:
            if term not in [flashcard.term for flashcard in flashcards]:
                break
            else:
                logging.info(f"The card \"{term}\" already exists. Try again:\n")
                term = input()
        logging.info("The definition of the card:")
        definition = input()
        while True:
            if definition not in [flashcard.definition for flashcard in flashcards]:
                break
            else:
                logging.info(f"The definition \"{definition}\" already exists. Try again:")
                definition = input()
        flashcards.append(Flashcard(term, definition))
        logging.info(f"The pair (\"{term}\":\"{definition}\") has been added.")

    elif choice == 'remove':
        logging.info("Which card?")
        card = input()
        if Flashcard.get_flashcard(flashcards, card):
            flashcards.remove(Flashcard.get_flashcard(flashcards, card))
            logging.info("The card has been removed.\n")
        else:
            logging.info(f"Can't remove \"{card}\": there is no such card.")

    elif choice == 'import':
        logging.info("File name:")
        file_name = input()
        if Path(file_name).is_file():
            with open(file_name, 'r') as json_file:
                inp_dict = json.load(json_file)
            for flashcard in Flashcard.from_dictionary(inp_dict):
                if flashcard.term not in [flashcard_.term for flashcard_ in flashcards]:
                    flashcards.append(flashcard)
                else:
                    Flashcard.get_flashcard(flashcards, term).definition = flashcard.definition
                    Flashcard.get_flashcard(flashcards, term).mistakes = flashcard.mistakes
            logging.info(f"{len(inp_dict.keys())} cards have been loaded.\n")
        else:
            logging.info("File not found.\n")

    elif choice == 'export':
        logging.info("File name:\n")
        file_name = input()
        with open(file_name, "w") as json_file:
            json.dump(Flashcard.to_dictionary(flashcards), json_file)
        logging.info(f"{len(flashcards)} cards have been saved.\n")

    elif choice == 'ask':
        logging.info("How many times to ask?")
        q = int(input())
        for i in range(q):
            card = random.choice(flashcards)
            logging.info(f"Print the definition of \"{card.term}\":")
            answer = input()
            if answer == card.definition:
                logging.info("Correct!\n")
            else:
                card.add_mistake()
                if answer in [flashcard.definition for flashcard in flashcards]:
                    logging.info(f"Wrong. The right answer is \"{card.definition}\", but your definition is correct for \""
                          f"{[flashcard.term for flashcard in flashcards][[flashcard.definition for flashcard in flashcards].index(answer)]}\".\n")
                else:
                    logging.info(f"Wrong. The right answer is \"{card.definition}\".\n")

    elif choice == 'exit':
        logging.info("Bye bye!")
        break

    elif choice == 'log':
        logging.info("File name:")
        file_name = input()
        shutil.copyfile('temp_log_file.log', file_name)
        logging.info("The log has been saved.")

    elif choice == 'hardest card':
        if not flashcards:
            logging.info("There are no cards with errors.\n")
        else:
            flashcards.sort(key=lambda x: -x.mistakes)
            if flashcards[0].mistakes == 0:
                logging.info("There are no cards with errors.\n")
            else:
                q = flashcards[0].mistakes
                if flashcards[1].mistakes != q:
                    logging.info(f"The hardest card is \"{flashcards[0].term}\". You have {q} errors answering it.\n")
                else:
                    hard_list = [flashcards[0].term, flashcards[1].term]
                    i = 2
                    while i < len(flashcards) and q == flashcards[i].mistakes:
                        hard_list.append(flashcards[i].term)
                        i += 1
                    output = ""
                    for elem in hard_list:
                        if hard_list.index(elem) < len(hard_list) - 1:
                            output += "\"" + elem + "\", "
                        else:
                            output += "\"" + elem + "\""
                    logging.info(f"The hardest cards are \"{output}\". You have {q} errors answering it.\n")

    elif choice == 'reset stats':
        for flashcard in flashcards:
            flashcard.reset()
        logging.info("Card statistics have been reset.")

    else:
        logging.info("Incorrect option. Try again!\n")