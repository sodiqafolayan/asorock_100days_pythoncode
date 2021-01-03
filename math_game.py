import time
import sys

add = "addition"
sub = "subtraction"
mul = "multiplication"
div = "division"

print("Welcome to simple math !!!")
time.sleep(3)
name = input("What is your name?: ")
time.sleep(3)
print(f"Cool!!! Thank you {name.title()}, you are now ready to have fun!!!")
time.sleep(5)
print("Give me few seconds to get your maths game.....")
time.sleep(5)
print("""
        Below are the available math operations
		1. Addition\n
		2. Subtraction\n
		3. Multiplication\n
		4. Division""")

time.sleep(5)
math_term = int(input("Enter a number from the above selection: "))
time.sleep(3)

if math_term == 1:
    print(f"Just a second please....we will commence your {add} shortly")
    first_num = int(input("Enter your first number: "))
    time.sleep(3)
    print("Cool!!!")
    second_num = int(input("Enter your second number: "))
    time.sleep(3)
    print("Awesome!!!")
    time.sleep(3)
    print("I want to make sure i give the correct answer")
    time.sleep(3)
    print(f"I am sure you know {add} can be tricky sometimes")
    time.sleep(3)
    print("Still thinking......")
    time.sleep(3)
    print("I am almost there, trust me .........")
    time.sleep(3)
    print("Yes!!! I got it, just wait for it")
    time.sleep(3)
    print("And here it is......")
    time.sleep(2)
    result = first_num + second_num
    print(result)

elif math_term == 2:
    print(f"Just a second please....we will commence your {sub} shortly")
    first_num = int(input("Enter your first number: "))
    time.sleep(3)
    print("Cool!!!")
    second_num = int(input("Enter your second number: "))
    time.sleep(3)
    print("Awesome!!!")
    time.sleep(3)
    print("I want to make sure i give the correct answer")
    time.sleep(3)
    print(f"I am sure you know {sub} can be tricky sometimes")
    time.sleep(3)
    print("Still thinking......")
    time.sleep(3)
    print("I am almost there, trust me .........")
    time.sleep(3)
    print("Yes!!! I got it, just wait for it")
    time.sleep(3)
    print("And here it is......")
    time.sleep(2)
    result = first_num - second_num
    print(result)

elif math_term == 3:
    print(f"Just a second please....we will commence your {mul} shortly")
    first_num = int(input("Enter your first number: "))
    time.sleep(3)
    print("Cool!!!")
    second_num = int(input("Enter your second number: "))
    time.sleep(3)
    print("Awesome!!!")
    time.sleep(3)
    print("I want to make sure i give the correct answer")
    time.sleep(3)
    print(f"I am sure you know {mul} can be tricky sometimes")
    time.sleep(3)
    print("Still thinking......")
    time.sleep(3)
    print("I am almost there, trust me .........")
    time.sleep(3)
    print("Yes!!! I got it, just wait for it")
    time.sleep(3)
    print("And here it is......")
    time.sleep(2)
    result = first_num * second_num
    print(result)

elif math_term == 4:
    print(f"Just a second please....we will commence your {div} shortly")
    first_num = int(input("Enter your first number: "))
    time.sleep(3)
    print("Cool!!!")
    second_num = int(input("Enter your second number: "))
    time.sleep(3)
    print("Awesome!!!")
    time.sleep(3)
    print("I want to make sure i give the correct answer")
    time.sleep(3)
    print(f"I am sure you know {div} can be tricky sometimes")
    time.sleep(3)
    print("Still thinking......")
    time.sleep(3)
    print("I am almost there, trust me .........")
    time.sleep(3)
    print("Yes!!! I got it, just wait for it")
    time.sleep(3)
    print("And here it is......")
    time.sleep(2)
    result = first_num / second_num
    print(result)
    # next_game = input("Will you like to play again (enter 1 for yes or 2 for): ? ")
    # how do i make the game go back up to start again
else:
    print("You entered a wrong selection")
    sys.exit()
    # next_game = input("Will you like to play again (enter 1 for yes or 2 for): ? ")

    # how do i make the game go back up to start again
