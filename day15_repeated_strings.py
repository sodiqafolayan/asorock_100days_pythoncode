# https://www.hackerrank.com/challenges/repeated-string/problem?filter=python3&filter_on=language&h_l=interview&page=1&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup


count = 0
s = input("Enter your word")
n = int(input("Enter your number of 'a' search"))
for item in s[:n+1]:
    if item == "a":
        count+=1
print(count)