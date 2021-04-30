import string

def caeser_cipher(): 
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
        elif direction == 'e' or direction == 'encode':
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