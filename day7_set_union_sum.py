"""
The students of District College have subscriptions to English and French newspapers. 
Some students have subscribed only to English, some have subscribed to only French and 
some have subscribed to both newspapers. You are given two sets of student roll numbers. 
One set has subscribed to the English newspaper, and the other set is subscribed to the 
French newspaper. The same student could be in both sets. Your task is to find the total 
number of students who have subscribed to at least one newspaper.
"""
n = int(input("How many students subscribes to English: "))
n_list = []
b_list = []
for i in range(1, n+1):
    c = int(input("Whats the student code: "))
    n_list.append(c)
b = int(input("How many students subscribes to French: "))
for i in range(1, b+1):
    d = int(input("Whats the student code: "))
    b_list.append(d)
print(n)
print(*n_list)
print(b)
print(*b_list)
u = set(n_list)
t = set(b_list)
print(sum(u | t))
