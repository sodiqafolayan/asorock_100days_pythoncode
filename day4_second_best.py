# This code pair student name and their respective scores and prints out the student
# name with the second best score


def second_best():
    nested_name_score = []
    a = int(input("How many students?: "))
    for i in range(1, a+1):
        name = input(f"({i}). Enter student name: ")
        score = float(input(f"What is {name} score? "))
        nested_name_score.append([name, score])
    print(nested_name_score)
    z = sorted([*set([item[-1] for item in nested_name_score])])
    print(z)
    for item in nested_name_score:
        if item[-1] == z[-1]:
            print(item[0])


second_best()
