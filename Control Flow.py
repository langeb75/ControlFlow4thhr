# Programmer: Mr. Lange
# Date: 10.11.2021
# Program: ATM Bank Transaction

"""
This program simulates an ATM utilizing If, Elif, & Else statements
Nesting If statements and refresh our Comparison & Logical Operators
"""

print("Welcome to Cash-R-Us Bank\nLet's take a moment to set up your account.\n")

# Set up account by asking users for their first & last names using Variables
firstName = input("What is your first name: ")
lastName = input("What is your last name: ")

print("\nWelcome to Cash-R-Us",firstName,lastName + ", we will now set up a security PIN on your account.\n")

# Set up a PIN - Personal Identification Number
pin = input("Please choose a 4-digit Personal Identification Number: ")

print("\nThank you",firstName + ", we see that you set your PIN to",pin)

print("\nWould you like to make a transaction through our Automated Teller Machine")
atm = input("Yes or No: ").lower()

if atm == "yes":
    print("\n***************************************************\n")

    # This part of the program will be asking users to complete a transaction through the ATM
    print("Please insert your ATM card\n")
    print("Welcome to Cash-R-Us ATM",firstName,lastName,"\n")
    userPIN = input("What is your four digit PIN: ")

    if pin == userPIN:
        balance = 674
        print("\nYour Balance: $" + str(balance))

        # Ask users what type of transaction they want - Withdrawal - Deposit
        typeOfTransaction = input("\nWould you like to make a Withdrawal, Deposit, or check your Balance\nW = Withdrawal or D = Deposit or B = Balance: ").lower()
        if typeOfTransaction == "w":
            withdrawalAmount = int(input("Enter amount of withdrawal: "))
            balance = balance - withdrawalAmount
            print("Your new balance is: $" + str(balance))
            
        elif typeOfTransaction == "d":
            depositAmount = int(input("Enter amount of your deposit: "))
            balance = balance + depositAmount
            print("Your new balance is: $" + str(balance))

    else:
        print("\nSorry",firstName,lastName,"your PIN doesn't match our records")


else:
    print("\nHave a wonderful day",firstName,lastName + ", please come back and visit soon.")
