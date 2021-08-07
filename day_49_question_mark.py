"""
Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers,
letters, and question marks, and check if there are exactly 3 question marks between every pair of two numbers
that add up to 10. If so, then your program should return the string true, otherwise it should return the string
false. If there aren't any two numbers that add up to 10 in the string, then your program should return false as
well. For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly
3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.
"""

if __name__ == '__main__':
    # This is an helper function that checks if the str has at least two str.isdigit() in it
    # If not True, then there is no point working on the string
    def two_or_more_digits_exist(str_para: str) -> bool:
        digit_count = [int(i) for i in str_para if i.isdigit()]
        return len(digit_count) >= 2

    # This is another helper function that returns index of the first str.isdigit() to be used
    # later in the main code. It is actually isn't really necessary to create this helper function
    # however, it helps with code clarity and reduces the number of code lines of the main body
    def first_digit_index(a_string: str) -> int:
        c = 0
        for i in a_string:
            if i.isdigit():
                c += a_string.index(i)
                return c
    """
    Algorithm
    1. Check is the len() of the parameter is at least 5. This is the minimum string lenght theat is required
        before we can even start checking if there exist 2 is digits which have 3 question marks within it
    2. Check if we have at least 2 str.digit() in the parameter
    3. Count the number of question marks within the parameter and be sure it is at least 3
    4. Get the index of the first digit within the parameter. This will be helpful to assess the digit
        itself and save it as a starting point of our summation. Plus, it will also ensure that our next digit 
        search will be after the first index
    5. We will quickly need to check that the lenght of the string from the first index to the end is >= 5 before proceeding
        This is to do a c=second check and be sure that we will have the possibility of at least 3 question marks and another 
        digit within that
    6. Save the first digit in the parameter inside a variable
    7. Start searching for the next digit within the parameter from after the index of the first digit
    8. If you find a digit, add it to the first digit, if it is == 10, count the number of question marks within it. If not == 3: return "false"
    9. If the condition in number 8 is met, the iteration will continue except untrue
    
    """

    def QuestionsMarks(strr):
        if len(strr) < 5 or not two_or_more_digits_exist(strr) \
                or strr.count("?") < 3:
            return "false"
        get_first_digit_index = first_digit_index(strr)
        if len(strr[get_first_digit_index:]) < 5:
            return "false"
        first_digit = int(strr[get_first_digit_index])
        check_starts = get_first_digit_index + 1
        while len(strr[check_starts:]) >= 4:
            for i in strr[check_starts:]:
                if i.isdigit() and first_digit + int(i) == 10:
                    result = strr[check_starts:strr.index(i)].count("?")
                    if result != 3:
                        return "false"
            return "true"
        return "false"


    ss = "arrb6???4xxbl5???eee5"
    aso = "2dmd???mdm8"
    print(QuestionsMarks(aso))
