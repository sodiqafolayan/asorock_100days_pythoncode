import time
import sys
"""
Design a software for bank system. There should be options like cash withdraw, cash credit and change
password. According to user input, the software should provide required output.Hint: Use if else statements
and functions.
"""

print("Welcome to Asorock's bank")
time.sleep(2)
print("See below available options:")
time.sleep(2)
print("""
Press the any number correspoding to the operation you want to perform\n
Press 1 for Cash Withrawal\n
Press 2 for Cash Credit\n
Press 3 to Change Password\n"""
      )
time.sleep(2)
operation = int(input("Enter your option from the above: "))

if operation == 1:
    amount = int(input("Please enter an amount to withraw: "))
    time.sleep(1)
    print(f"Here is your ${amount}. Thank you for banking with us")
elif operation == 2:
    amount = int(input("Please enter cash credit amount: "))
    time.sleep(1)
    print(
        f"Your cash credit of ${amount} is successful. Thank you for banking with us")
elif operation == 3:
    for i in range(1, 3):
        password = input(f"({i}). Enter you new password: ")
        # If the password isn't the same, how do i catch it and request the user to re-enter the password?
    time.sleep(1)
    print("We are now processing your password change......")
    time.sleep(2)
    print("Your password is now succesfully changed. Thank you for banking with us")
else:
    time.sleep(2)
    print("You inputed an invalid number. Please try again next time")
    sys.exit()
    # Instead of exiting, i will like to give the user the option to try again
