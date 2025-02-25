score = int( input("Enter a score: ") )

if score >= 90:
    print("Grade: A")
else:
    if 80 <= score <= 89:
        print("Grade: B")
    else:
        if 70 <= score <= 79:
            print("Grade: C")
        else:
            print('Grade: F')

