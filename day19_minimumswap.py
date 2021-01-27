# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
arr = [7, 3, 1, 5, 4, 6, 2]
def minimumSwaps(a_list):
    print(len(a_list))
    print(*a_list)
    list_sort = sorted(a_list)
    enu_a_list = [[k+1, v] for k,v in (enumerate(a_list))]
    enu_a_list_sort = [[k+1, v] for k,v in (enumerate(list_sort))]
    n = 0
    for item in enu_a_list:
        for i in enu_a_list_sort:
            if item[-1] == i[-1]:
                item_ind = enu_a_list.index(item)
                i_ind = enu_a_list_sort.index(i)
                if item_ind != i_ind:
                    n+=1
                else:
                    n = n
    return n-1
    

print(minimumSwaps(arr))