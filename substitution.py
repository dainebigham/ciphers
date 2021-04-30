import sys
import string
from collections import Counter

def substitution():
    # ensure correct number of arguments has been given
    if len(sys.argv) != 2:
        print("USAGE: python substitution.py KEY")

    #call function to check if key is valid
    if is_valid_key(sys.argv[1]) is False:
        return 1
    else: 


def is_valid_key(key):
    # count if any character in the key are repeats
    result = Counter(key)
    # if key is more or less than 26 characters throw error
    if len(key) != 26:
        print("Key must be 26 characters long")
        return False
    # if key contains numbers, symbols, or spaces throw error
    elif(key.isalpha() != True):
       print("Key must contain only upper and lowercase letters")
       return False
    else:
        # loop through result dictionary
        for item in result:
            # if an item has been counted more than once throw error
            if result[item] > 1:
                print("No repeating characters allowed")
        return False
    
    return True

substitution()