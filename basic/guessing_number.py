import random 
secret=random.randint(0,9)

print(secret)

print("I have selected a secret number from 0 to 9 in my mind.") 
print("Now start guessing the number. You are given 3 chances.")

guessnumber = input("What is the secret number? Type the number here : ")

if int(guessnumber) < secret: 
    print("The number " + guessnumber + " entered is quite close !") 
    guessnumber = input("Try second round. Type the number here : ") 

if int(guessnumber) < secret: 
    print("The number " + guessnumber + " entered is quite close !") 
    guessnumber = input("Try third round. Type the number here : ") 

if int(guessnumber) < secret: 
    print("The number " + guessnumber + " entered is quite close !") 

if int(guessnumber) == secret: 
    print("Congratulations!!You have guessed the secret number correctly") 
else: 
    print("Sorry the number guessed is wrong...") 

print("The secret number in my mind is " + str(secret) )
