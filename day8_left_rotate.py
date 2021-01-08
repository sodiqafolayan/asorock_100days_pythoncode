from collections import deque
# numberList = [111, 111, 333, 333, 555, 555, 302, 302, 330]
# Given numberList above, write a python function that left rotate the items in numberList from index 0 in x
# number of times. x will be derived from use input. For exapmple, if user input x == 4, your new list will be
# [555, 555, 302, 302, 330, 111, 111, 333, 333]

numberList = [111, 111, 333, 333, 555, 555, 302, 302, 330]
d = int(input("How many times do you want to left rotate your list? "))
# Option 1
second_list = numberList[d:] + numberList[:d]
print(second_list)

# Option 2
dq = deque(numberList)
dq.rotate(-d)  # this left rotate, to rigth rotate, we will have dq.rotate(d)
deque_to_list = list(dq)
print(deque_to_list)

# Option 3
for item in range(d):
    numberList.append(numberList.pop(0))
print(numberList)
