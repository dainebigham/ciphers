import string

def caeser_cipher(): 
    print("\nWelcome to the Caeser Cipher")
    print("")
    print("-------------------------------------------------------------------------")
    print("")
    print("The Caesar cipher is one of the earliest known and simplest ciphers, named after Julius Caesar, who apparently used it to communicate with his generals.\nIt is a type of substitution cipher in which each letter in the plaintext is 'shifted' a certain number of places down the alphabet.\nFor example, with a shift of 1, A would be replaced by B, B would become C, and so on.")
    print("")
    print("-------------------------------------------------------------------------")
    print("")
    input("Press ENTER to continue...")

    # infinite loop to ensure correct input
    while True:
        # decide whether you are encrypting or decrypting and convert input to lowercase
        direction = input("\nType '(e)ncode' to encrypt, and '(d)ecode' to decrypt:\n").lower()

        # if input is correct
        if direction == 'encode' or direction == 'e' or direction == 'decode' or direction == 'd':
            # enter message to de/encrypt
            text = input("Message to decode:\n").lower()
            # infinite loop to ensure correct input type/value
            while True:
                try:
                    # enter amount of shift for encryption
                    shift = int(input("Enter the amount of 'shift':\n"))
                    break
                except (ValueError, TypeError):
                    print("Please enter a number")
            # call function to en/decrypt
            caeser(text, shift, direction)
            break
        else:
            print("Incorrect input. Type '(e)ncode' for encryption, or '(d)ecode' for decryption")

def caeser(text, number, code):
    # create a list of lowercase letters to rotate through
    alpha = list(string.ascii_lowercase)

caeser_cipher()