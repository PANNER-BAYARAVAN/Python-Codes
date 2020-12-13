try:
    number = int(input("Enter a number between 1 - 10 :"))
except ValueError:
    print ("Only numbers please")
    sys.exit()

print ("The number entered is : ", number)
