year_input = input("Enter a year: ")
year_input = int(year_input)

if year_input % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")