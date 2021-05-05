import string
import sys

def caeser_cipher(): 
    # ensure correct number of arguments has been given
    if len(sys.argv) != 3:
        print("USAGE: python substitution.py -(e)ncrypt/-(d)ecrypt shift")
        return 1
    direction = sys.argv[1].lower()
    shift = int(sys.argv[2])

    # ensure correct input
    if direction == '-e' or direction == '-encode' or direction == '-d' or direction == '-decode':
        text = input("Message to encode: ").lower()
        caeser(text, shift, direction)
    else: 
        print("USAGE: python substitution.py -(e)ncrypt/-(d)ecrypt shift")
        return 1

def caeser(text, shift, direction):
    # create a list of lowercase letters to rotate through
    alpha = list(string.ascii_lowercase)
    coded = ""
    
    # loop through each character in the input message
    for ch in text:
        # if the character is not in alpha list then just add it to output text
        if ch not in alpha:
            coded += ch
        # if we are encoding message
        elif direction == '-e' or direction == '-encode':
            # find the location of that letter in the alpha array and add amount of shift
            alpha_index = alpha.index(ch) + shift
            # if this length is greater than the array length, minus by 26 to bring index back in line with alphabet
            if alpha_index > 25:
                alpha_index -= 26
            # add shifted letter to the output string
            coded += alpha[alpha_index]
            # else do the same but in reverse
        else:
            alpha_index = alpha.index(ch) - shift
            
            if alpha_index > 25:
                alpha_index += 26

            coded += alpha[alpha_index]
    print(f"Your message is {coded}")

caeser_cipher()