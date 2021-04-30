import sys
import string
from collections import Counter

def substitution_cipher():
    # ensure correct number of arguments has been given
    if len(sys.argv) != 3:
        print("USAGE: python encrypt/decrypt substitution.py KEY")
        return 1
    arg1 = sys.argv[1].lower()
    arg2 = sys.argv[2].lower()

    # check if arguments are valid
    if arg1 == 'encrypt' or arg1 == 'decrypt' or is_valid_key(arg2) is True:
        substitution(arg1, arg2)
    else:
        return 2

def substitution(code, key):
    # store the alphabet in a variable for easy indexing, create empty cariable to hold coded message, and ask user for message
    alpha = string.ascii_lowercase

    if code == 'encrypt':
        encoded = ""
        message = input("Enter message to encrypt: ").lower()

        # for each character in the message, find the messages index in the alphabet and store it in temp variable
        for ch in message:
            if ch in alpha:
                alpha_temp = alpha.index(ch)
                # then create a temp variable to store the letter of the same index in the key variable and add it to the coded message
                key_temp = key[alpha_temp]
                encoded += key_temp
            else:
                encoded += ch

        print(f"Your coded message is: {encoded}")
    elif code == 'decrypt':
        decoded = ""
        message = input("Enter message to decrypt: ").lower()

        # same as above but in reverse
        for ch in message:
            if ch in alpha:
                key_temp = key.index(ch)
                alpha_temp = alpha[key_temp]
                decoded += alpha_temp
            else:
                decoded += ch
        
        print(f"Your decoded message is: {decoded}")

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