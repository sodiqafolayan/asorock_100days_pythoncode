
# Task
# The students of District College have subscriptions to English and French newspapers.
# Some students have subscribed only to English, some have subscribed only to French,
# and some have subscribed to both newspapers. You are given two sets of student roll numbers.
# One set has subscribed to the English newspaper, one set has subscribed to the French newspaper.
# Your task is to find the total number of students who have subscribed to both newspapers.

n_list = []
b_list = []
n = int(input("How many students subscribed to English? "))
for i in range(1, n+1):
    n_student = int(input(f"What is student {i} roll number: "))
    n_list.append(n_student)
b = int(input("How many students subscribed to French? "))
for i in range(1, b+1):
    b_student = int(input(f"What is student {i} roll number: "))
    b_list.append(b_student)
print(n)
print(*n_list)
print(b)
print(*b_list)
c = set(n_list).intersection(set(b_list))
print(len(c))
