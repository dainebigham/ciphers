import sys
import string
from collections import Counter

def substitution_cipher():
    # ensure correct number of arguments has been given
    if len(sys.argv) != 2:
        print("USAGE: python substitution.py KEY")
    #call function to check if key is valid
    
    if is_valid_key(sys.argv[1]) is True:
        substitution(sys.argv[1])
    else:
        return 1

def substitution(key):
    alpha = string.ascii_lowercase
    input("Enter message to encrypt: ").lower()
    print(alpha)

def is_valid_key(key):
    # count if any characters in the key are repeats and create duplicate check var
    result = Counter(key)
    duplicate = False
    # loop through result dictionary
    for item in result:
        # if an item has been counted more than once duplicate check is true
        if result[item] > 1:
            duplicate = True

    # if key is more or less than 26 characters throw error
    if len(key) != 26:
        print("Key must be 26 characters long")
        return False
    # if key contains numbers, symbols, or spaces throw error
    elif key.isalpha() != True:
       print("Key must contain only upper and lowercase letters")
       return False
    # if duplicates were dedected throw error
    elif duplicate == True:
        print("No repeating characters allowed")
        return False
    else:
        return True

substitution_cipher()