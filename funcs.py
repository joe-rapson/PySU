def string_split(string): #function to split the text into an array 
    return [char for char in string]

def roll_over(code): #if the character exceeds the maximum for the case
    correct_key = chr((code - 26))
    return correct_key

def upper_lower(string):
    if ((65 <= ord(string)) & (90 >= ord(string))): #uppercase letters
        return "upper"
    elif((97 <= ord(string)) & (122 >= ord(string))): #lowercase letters
        return "lower"

def alphabetPos(string):
    if (upper_lower(string) == "upper"):
        pos = ord(string) - 65
        return pos
    else:
        pos = ord(string) - 97
        return pos