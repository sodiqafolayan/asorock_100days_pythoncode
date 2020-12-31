# 1. What is the output of the following code?
import random
nums = set([1, 1, 2, 3, 3, 3, 4, 4])
print(len(nums))
# Output: 4

# 2. What will be the output?
d = {"john": 40, "peter": 45}
print(list(d.keys()))
# Output: ['john', 'peter']

"""
3. A website requires a user to input username and password to register. Write a program
to check the validity of password given by user. Following are the criteria for checking
password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
"""


def password_validation(password=input("Please enter your password: ")):

    SpecialSym = ['$', '@', '#', '%']
    val = True

    if len(password) < 6:
        print('length should be at least 6')
        val = False

    if len(password) > 12:
        print('length should be not be greater than 12')
        val = False

    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in SpecialSym for char in password):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val


password_validation()


# 4. Write a for loop that prints all elements of a list and their position in the list
a = [4, 7, 3, 2, 5, 9]
b = [*enumerate(a)]
print(b)
"""
5. Please write a program which accepts a string from console and print the
characters that have even indexes.
 Example: If the following string is given as input to the program:
 H1e2l3l4o5w6o7r8l9d
 Then, the output of the program should be:
 Helloworld
"""
u = []
user_input = input("Please enter a string: ")

for item in user_input:
    if user_input.index(item) % 2 == 0:
        u.append(item)
print(" ".join(u))


"""
6. Please write a program which accepts a string from console and print it in reverse
order.
 Example: If the following string is given as input to the program:
 rise to vote sir
 Then, the output of the program should be:
 ris etov ot esir
"""
user_input = input("Please enter a string: ")
print(user_input[::-1])

"""
7 Please write a program which count and print the numbers of each character in a
string input by console.
Example: If the following string is given as input to the program:
abcdefgabc
Then, the output of the program should be:
a,2
c,2
b,2
e,1
d,1
g,1
f,1
"""
user_input = input("Please enter a string: ")
for item in user_input:
    print(item, user_input.count(item))

"""
8. With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a
program to make a list whose elements are intersection of the above given lists.
"""
a = [1, 3, 6, 24, 88, 78, 35, 55]
b = [12, 24, 35, 24, 88, 120, 155]
common_item = [x for x in a if x in b]
print(common_item)

"""
9. With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this
list after removing all duplicate values with original order reserved.
"""
my_list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
print(list(set(reversed(my_list)))[::-1])

"""
10.By using list comprehension, please write a program to print the list after removing
the value 24 in [12,24,35,24,88,120,155].
"""
com_list = [12, 24, 35, 24, 88, 120, 155]
rem_list = [item for item in com_list if item != 24]
print(rem_list)

"""
By using list comprehension, please write a program to print the list after removing
the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
"""
your_list = [12, 24, 35, 70, 88, 120, 155]
new_list = []


def item_remove(a_list):
    del a_list[0]
    del a_list[4:6]
    return a_list


print(item_remove(your_list))

"""
12.By using list comprehension, please write a program to print the list after removing
delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
"""
div_list = [12, 24, 35, 70, 88, 120, 155]
div_5_7 = [item for item in div_list if item % 5 != 0 and item % 7 != 0]
print(div_5_7)
