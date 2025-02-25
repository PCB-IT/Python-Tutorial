side_1 = int(input("Side 1: "))
side_2 = int(input("Side 2: "))
side_3 = int(input("Side 3: "))

if side_1 + side_2 > side_3:
    print("It is valid")

    if side_1 == side_2 and side_2 == side_3:
        print("Equilateral")
    else:
        print("Not an equilateral")

        if side_1 == side_2 or side_2 == side_3 or side_1 == side_3:
            print("Isosceles")
        else:
            print("Not an Isosceles")

            if side_1 != side_2 and side_2 != side_3:
                print("Scalene")

        print("Concluded")
else:
    print("Not valid")

print("End of program")