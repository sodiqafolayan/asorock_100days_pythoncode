"""
Your friend has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. 
She asked for your help. You pick the stamps one by one from a stack of N country stamps.
Find the total number of distinct country stamps.

Input Format

The first line contains an integer N, the total number of country stamps.
The next N lines contains the name of the country where the stamp is from.
Constraints


Output Format

Output the total number of distinct country stamps on a single line.
"""
stamp_countries = []
n = int(input("How many stamps do you have?: "))
for i in range(1, n+1):
    stamp_countries.append(input("Enter stamp country: "))
for item in stamp_countries:
    print(item)

vv = len(set(stamp_countries))
print(vv)
