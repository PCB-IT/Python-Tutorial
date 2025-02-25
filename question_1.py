number = int(input("Enter a number: "))

if number > 0:
    if number > 100:
        print("Positive and greater than 100")
    elif number == 0:
        print("Zero")
    else:
        print("Positive but not greater than 100")
else:
    if number < -50:
        print("Negative and less than -50")
    else:
        print("Negative but not less than -50")

print("End of program")