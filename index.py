from vSqu import vSqu
from funcs import string_split, upper_lower, roll_over, alphabetPos

def caesar(plaintext, key): #caesar encipher algorithm
    plain_array = string_split(plaintext) #so that characters can be individually altered
    cipher_array = []
    realKey = int(key) % 26 # so that keys do not exceed a shift of 26 places
    for char in plain_array:
        case = upper_lower(char)
        shifted_charcode = int(ord(char) + int(realKey))
        if (((case == "upper") & (shifted_charcode > 90))| ((case == "lower") & (shifted_charcode > 122))):
            shifted_char = chr(shifted_charcode)
            shifted_char = str(roll_over(shifted_charcode))
            cipher_array.append(shifted_char)
        else:
            shifted_char = chr(shifted_charcode)
            cipher_array.append(shifted_char)
    print(''.join(cipher_array))

def vigenere(plaintext, key):
    plain_array = string_split(plaintext)
    key_array = string_split(key)
    cipher_array = []
    key_pos = 0
    for each in plain_array:
        plain_index = int(alphabetPos(each))
        key_index = alphabetPos(key_array[key_pos])
        cipher_array.append(vSqu[plain_index][key_index])
        key_pos += 1
        if (key_pos >= len(key_array)):
            key_pos = 0
    ciphertext =''.join(cipher_array)
    return ciphertext

encode_decode = float(input("Would you like to 1. encode or 2. decode a message?"))
if (encode_decode != 3): #so i can skip through prompts for testing
    cipher_selected = float(input("Which cipher are you using? 1 - Caesar, 2 - Vigenere"))
if (encode_decode == 1): #user enters text
    plaintext = input("What text would you like to encode?")
    if (cipher_selected == 1):
        key = input("How many characters will the message be shifted by?")
        caesar(plaintext, key)
    elif(cipher_selected == 2 ):
        key = input("What keyword would you like to encipher the message by?")
        print("Your enciphered text is", vigenere(plaintext, key))