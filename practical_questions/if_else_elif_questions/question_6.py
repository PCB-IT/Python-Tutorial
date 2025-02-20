password = input("Enter password: ")
store_password = "RSA"

if len(password) == 0:
    print("No password given")
elif password == store_password:
    print("Password is correct")
else:
    print("Incorrect password")