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
num = int(input("Input the number of cards:\n"))

flashcards = {}
for i in range(num):
    term = input(f"The term for card #{i + 1}:\n")
    while True:
        if term not in flashcards.keys():
            break
        else:
            term = input(f"The term \"{term}\" already exists. Try again:\n")
    definition = input(f"The definition for card #{i + 1}:\n")
    while True:
        if definition not in flashcards.values():
            break
        else:
            definition = input(f"The definition \"{definition}\" already exists. Try again:\n")
    flashcards[term] = definition

for key, value in flashcards.items():
    answer = input(f"Print the definition of \"{key}\":\n")
    if answer == value:
        print("Correct!")
    elif answer in flashcards.values():
        print(f"Wrong. The right answer is \"{value}\", but your definition is correct for "
              f"{list(flashcards.keys())[list(flashcards.values()).index(answer)]}")
    else:
        print(f"Wrong. The right answer is \"{value}\".")