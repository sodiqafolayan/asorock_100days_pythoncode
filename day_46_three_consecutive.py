"""
This code checks if there 3 consecutive items within a string and the sum
of the item before and after the 3 consecutive items (if digits) is = 10
"""

if __name__ == '__main__':
    def three_consecutive_in_between(strr, item):
        for i in strr:
            if i != strr[0] and strr.index(i) < len(strr) - 3 \
                    and i == item and strr[strr.index(i) + 1] == item \
                    and strr[strr.index(i) + 2] == item \
                    and strr[strr.index(i) - 1].isdigit() \
                    and strr[strr.index(i) + 3].isdigit() \
                    and int(strr[strr.index(i) - 1]) + int(strr[strr.index(i) + 3]) == 10:
                return "true"
        return "false"


    print(three_consecutive_in_between("acc?7??sss?3rr1??????5", "?"))
    print(three_consecutive_in_between("aa6?9", "?"))
