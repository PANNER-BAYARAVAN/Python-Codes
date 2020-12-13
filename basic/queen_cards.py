import random
queencard=random.randint(1,3)
'print(queencard)'
print(" -------   -------   ------- ")
print("|       | |       | |       |")
print("|   1   | |   2   | |   3   |")
print("|       | |       | |       |")
print("|       | |       | |       |")
print(" -------   -------   -------")
print("The queen cards are shuffled")
print("Now start guessing where is the queen card.")
guesscard = input("Where is the Queen Card? Type the card number here : ")
if int(guesscard) == queencard:
    print("Congratulations!!You have guessed the Queen Card correctly")
else:
    print("Sorry the card number guessed is wrong...")
