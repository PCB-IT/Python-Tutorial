year = int(input("What is the current year?"))

if year % 4 == 0:
    print("Yes, it is a leap year.")
else:
    if year % 400 == 0:
        print("Yes, it is a leap year.")
    else:
        print("No, not a leap year")