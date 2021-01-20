# Write a program that returns zero if the summation of any substrings 
# == 0, else return the sum


# Option 1
a = [3, 0, -3, 4, 9, 10]
count = 0
i = 0
for item in a:
    count += a[i]
    i+=1
    if count == 0:
        break
        print(count)
print(count)

# Option 2
def zerosubarray(my_list):
    count = 0
    i = 0
    for item in a:
        count += a[i]
        i+=1
        if count == 0:
            break
            return count
        
    return count

print(zerosubarray(a))