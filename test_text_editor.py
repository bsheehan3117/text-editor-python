'''
    CS5001
    Spring 2023
    HW5

    Brendan Sheehan

    This program tests the append, add, substitute, scramble, and unscramble functions.
'''

from text_editor import append
from text_editor import add
from text_editor import substitute
from text_editor import scramble
from text_editor import unscramble

def test_text_editors():
    '''
    Function: test_text_editors
    This function is the test driver for the test_append,
    test_add, test_substitute, test_scramble, and test_unscramble
    functions.
    Parameters: none.
    Returns: test resutlts for the above functions
    '''
    # test append
    print("Tests for append")
    # test 1 basic add to a sentence
    test_append("It is nice outside", "today", "It is nice outside today")
    # test 2 empty first parameter
    test_append("", "It is nice outside", "It is nice outside")
    # test 3 empty second parameter
    test_append("It is nice outside", "", "It is nice outside")
    # test 4 white space at end of current text input
    test_append("It is nice outside ", "today", "It is nice outside today")
    # test 5 sentence with punctuation
    test_append("Today it is nice outside.", "Yes, it is!", "Today is it nice outside. Yes it is!")

    # test add
    print("Tests for add")
    # test 1 add a word to a sentence
    test_add("It is nice outside.", "not", 2, "It is not nice outside")
    # test 2 add two words with a space
    test_add("It is nice outside", "this afternoon", 4, "It is nice outside this afternoon")
    # test 3 add with a negative position input
    test_add("It is nice outside", "Because", -3, "Because it is nice outside")
    # test 4 add with a position input > len str
    test_add("It is nice outside", "today", 7, "It is nice outside today")
    # test 5 preserve punctuation
    test_add("It is nice outside!", "YAY!", 5, "It is nice outside! YAY!")

    # test substitute
    print("Tests for substitute")
    # test 1 swap a word
    test_substitute("It is nice outside today", "nice", "gross", "It is gross outside today")
    # test 2 swap a word with punctuation
    test_substitute("It is nice outside today", "is", "isn't", "It isn't nice outside today")
    # test 3 word not found
    test_substitute("It is nice outside today", "gross", "gross", "It is nice outside today")

    # test scramble
    print("Tests for scramble")
    # test 1 scramble lowercase
    test_scramble("defg", "fghi")
    # test 2 scramble uppercase
    test_scramble("DEFG", "FGHI")
    # test 3 scramble with punctuation the same
    test_scramble("DE:FG", "FG:HI")
    # test 4 scramble with y and z wrap around lowercase
    test_scramble("yz", "ab")
    # test 5 scramble with Y and Z wrap around uppercase
    test_scramble("YZ", "AB")

    # test unscramble
    print("Tests for unscramble")
    # test 1 unscramble lowercase
    test_unscramble("fghi", "defg")
    # test 2 unscramble uppercase
    test_unscramble("FGHI", "DEFG")
    # test 3 unscramble with punctuation the same
    test_unscramble("FG:HI", "DE:FG")
    # test 4 unscramble with a and b wrap around lowercase
    test_unscramble("ab", "yz")
    # test 5 unscramble with A and B wrap around uppercase
    test_unscramble("AB", "YZ")
    
def test_append(current_text: str, new_text: str, expected) -> str:

    '''
    Function: test_append
    Adds text to the end of the initial provided text and returns the
    new string
    Parameters: current_text: the initial provided text
    new_text: test to be added to the end of a string
    return: nothing, print actual vs expected
    '''
    
    actual = append(current_text, new_text)
    print("\tExpected = ", expected)
    print("\tResult = ", actual)
    
def test_add(current_text: str, new_text: str, start:int, expected) -> str:

    '''
    Function: test_add
    adds a string to a chosen position in the current text input
    Parameters: current_text: the initial provided text
    new_text: a string to be added to the current text
    start: the location in the string to add the new text
    return: nothing, print actual vs expected
    '''
    actual = add(current_text, new_text, start)
    print("\tExpected = ", expected)
    print("\tResult = ", actual)    

def test_substitute(current_text: str, word: str, new_word: str, expected) -> str:

    '''
    Function: test_add
    changes a word in a given text to another word and returns the
    updated text
    Parameters: current_text: the initial provided text
    word: a word in the initial text to be replaced
    new_word: a word chosen to replace the initial word
    return: nothing, print actual vs expected
    '''
    actual = substitute(current_text, word, new_word)
    print("\tExpected = ", expected)
    print("\tResult = ", actual)  

def test_scramble(current_text: str, expected) -> str:

    '''
    Function: test_scramble
    changes each letter in a string to a letter that is
    2 letters after it.
    Parameters: current_text: the text to be changed
    return: nothing, print actual vs expected
    '''
    actual = scramble(current_text)
    print("\tExpected = ", expected)
    print("\tResult = ", actual)

def test_unscramble(current_text: str, expected) -> str:

    '''
    Function: test_unscramble
    changes each letter in a string to a letter that is
    2 letters before it.
    Parameters: current_text: the text to be changed
    return: nothing, print actual vs expected
    '''
    actual = unscramble(current_text)
    print("\tExpected = ", expected)
    print("\tResult = ", actual)

def main():

    test_text_editors()
    
if __name__ == "__main__":    
    main()
