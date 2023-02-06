# Welcome to GUESSING GAME
"""
-The game revolves around guessing a number between two
 numbers you enter with the number of attempts you want
-You should play this game with your freind and make sure that the right number is invisible
"""
""""""""""""""""""""""""""""""


"""
get_data()
Get data from the user and make sure that the right number lied between the two number
by using if_right_in_range().
And send these data as a parameter to gussing(). 
And send the return of gussing to if_win_and_need_more().
"""


def get_data():
    print("G U E S S I N G G A M E 🤔🤔")
    first_num = int(input("Enter first number  : "))
    second_num = int(input("Enter second number : "))
    right_num = int(input("Enter The right between 1st & 2nd number :"))
    num_of_attepmts = int(input("Enter number of attempts :"))

    while if_right_in_range(right_num, first_num, second_num) == False:
        right_num = int(input("Enter The right between 1st & 2nd number :"))

    x = guessing(first_num, second_num, right_num, num_of_attepmts)
    if_win_and_need_more(x)


"""
if_right_in_range()
This function takes  the 1st & 2nd & right numbers that entered from the user
and test that the right number lied between the 1st & 2nd and return true or false. 
"""


def if_right_in_range(right_num, first_num, second_num):
    if (right_num >= first_num and right_num <= second_num) or (right_num <= first_num and right_num >= second_num):
        return True
    else:
        return False


"""
guessing()
Get the first_num, second_num, right_num, num_of_attepmts numbers as parameters 
and make some operation on these numbers
"""


def guessing(first_num, second_num, right_num, num_of_attepmts):
    guess_count = 0
    guessed_num = ""
    out_of_attempts = False
    while (guessed_num != right_num and not out_of_attempts):
        if (guess_count < num_of_attepmts):
            guessed_num = int(input("Enter your guess :"))
            guess_count += 1
        else:
            out_of_attempts = True
            return out_of_attempts
    return out_of_attempts


"""
Get a return_of_guessing as a parameter and check if that parameter equal true or not.
In the main IF we made if condition for asking the user if need to continue.
"""


def if_win_and_need_more(return_of_guessing):

    if (return_of_guessing):
        x = input("Oh sorry you lost 😔, want to try again (yes/no)?!").lower()
        if (x == "yes"):
            get_data()
        else:
            print("Thank you , see you later 👋 ")
    else:
        x = input(
            "CONGRATULATION YOU WIN!! 🥇 , want to try again (yes/no)?!").lower()
        if (x == "yes"):
            get_data()
        else:
            print("Thank you , see you later 👋 ")


"""
Calling get_data()
"""
get_data()

# THANK YOU !
