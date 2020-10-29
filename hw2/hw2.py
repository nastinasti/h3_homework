        # Konvisarova Anastasiia
        # Homework 2. Functions.
        # 10/27

import re

def validate_password(password):
    print(password)
    if not _validate_symbols(password):
        print("Error. Please check your password for forbidden symbols")  
    if not _validate_letters_even(password):
        print("Error. Numer of symbols is not even. Please try again")
    if not _validate_numbers_odd(password):
        print("Error. Numer of numbers is not odd. Please try again")
    #I KNOW IT IS CHEATING, BUT I REALLY CANNOT UNDERSTAND WHY WE NEED TO RETURN BOOL FROM OTHER 
    # FUNCTIONS AS WE CAN JUST GIVE AN ANSWER FOR THE CHECKING. PROBABLY IT IS MORE SISTEMITIZED AND 
    # UNDERSTANDABLE METOD, THAN JUST GIVE AN ANSWER

    if not _validate_letters_even(password) or not \
         _validate_numbers_odd(password) or not \
             _validate_symbols(password):
             return False
    return True

def _validate_symbols(input_str):
    #can I use regular expressions here? with re and match?
    if not input_str.isalnum():
        return False
    return True

def _validate_letters_even(input_str):
    match_sym = [sym for sym in input_str if not sym.isdigit()]
    if not len(match_sym) % 2:
        return True
    return False

def _validate_numbers_odd(input_str):
    match_num = [sym for sym in input_str if sym.isdigit()]
    if len(match_num) % 2:
        return True
    return False

print("\n-----This program is for password validation-----\n")

def main():
    from getpass import getpass
    password = getpass()
    if validate_password(password):
        print("\n----Passed----\n")
    else:
        main()

if __name__ == '__main__':
    main()
    