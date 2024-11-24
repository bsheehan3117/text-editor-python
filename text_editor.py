'''
    CS5001
    Spring 2023
    HW5
    
    Brendan Sheehan

    These are functions which modify a provided text.
    Functions include: append, substitute, add, scramble, unscramble
'''

def append(current_text: str, new_text: str) -> str:

    '''
    Function: append
    Adds text to the end of the initial provided text and returns the
    new string
    Parameters: current_text: the initial provided text
    new_text: test to be added to the end of a string
    Returns: string with new text appended
    Preconditions: if new text is empty, return current text
    if current text is empty, return new text
    '''
    # if new text is empty return current text
    if new_text == "":
        return current_text
    
    # make a copy of current text
    copy_str = ""
    copy_str = copy_str + current_text

    # append new text to string, if current text is blank,
    # no space required
    
    if current_text == "" or current_text[-1] == " ":
        appended_str = copy_str + new_text
        return appended_str

    else:
        appended_str = copy_str + " " + new_text

        return appended_str

def substitute(current_text: str, word: str, new_word: str) -> str:

    '''
    Function: substitute
    changes a word in a given text to another word and returns the
    updated text
    Parameters: current_text: the initial provided text
    word: a word in the initial text to be replaced
    new_word: a word chosen to replace the initial word
    Returns: string with updated text
    conditions: if word not found, return current text
    '''
    
    # make a copy of current text
    copy_str = ""
    copy_str = copy_str + current_text

    # split string into list for iteration
    copy_str = copy_str.split(" ")

    for i in range(len(copy_str)):
        if copy_str[i] == word:
            copy_str[i] = new_word

    copy_str = " ".join(copy_str)
    
    return copy_str

def add(current_text: str, new_text: str, start:int) -> str:

    '''
    Function: add
    adds a string to a chosen position in the current text input
    Parameters: current_text: the initial provided text
    new_text: a string to be added to the current text
    start: the location in the string to add the new text
    Returns: string with updated text
    '''
    if start < 0:
        start = 0
    
    # make a copy of current text
    copy_str = ""
    copy_str = copy_str + current_text

    # split copy of current text into a list
    copy_str = copy_str.split(" ")

    # insert new text into specified position in list
    copy_str.insert(start, new_text)

    # convert list to str and return new str
    new_str = ""

    for element in copy_str:
        new_str += element + " "

    # remove white space at end of string
    new_str = new_str.rstrip()
    
    return new_str

def scramble(current_text: str) -> str:
    '''
    Function: scramble
    changes each letter in a string to a letter that is
    2 letters after it.
    Parameters: current_text: the text to be changed
    Returns: string with scrambled text
    Special conditions: "Y" must return "A", "Z" must return "B"
    "y" must return "a", "z" must return "b"
    '''

    # make a copy of current text and an empty string
    str = current_text
    new_string = ''

    # if characters in a string are letters, change to ascii
    # and add two then convert back to letters
    # else, leave the index the same
    for i in range(len(str)):
        if str[i].isalpha():
            new_string += chr(ord(str[i]) + 2)
        else:
            new_string += str[i]

    # account for wraparound for characters Y,y,Z,z
    # replace result in new string with correct characters
    # for these four circumstances, return new string
    new_string = new_string.replace("[", "A")
    new_string = new_string.replace("{", "a")
    new_string = new_string.replace("\\", "B")
    new_string = new_string.replace("|", "b")
    
    return new_string

def unscramble(current_text: str) -> str:

    '''
    Function: unscramble
    changes each letter in a string to a letter that is
    2 letters before it.
    Parameters: current_text: the text to be changed
    Returns: string with unscrambled text
    Special conditions: "A" must return "Y", "B" must return "Z"
    "a" must return "y", "b" must return "z"
    '''
    
    # make a copy of current text & empty str
    str = current_text
    new_string = ''

    # if characters in a string are letters, change to ascii
    # and subtract two then convert back to letters
    # else, leave the index the same
    for i in range(len(str)):
        if str[i].isalpha():
            new_string += chr(ord(str[i]) - 2)
        else:
            new_string += str[i]

    # account for wraparound for characters A,a,B,b
    # replace result in new string with correct characters
    # for these four circumstances, return new string
    new_string = new_string.replace("_", "y")
    new_string = new_string.replace("`", "z")
    new_string = new_string.replace("?", "Y")
    new_string = new_string.replace("@", "Z")
    
    return new_string
