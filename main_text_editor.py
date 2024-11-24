'''
    CS5001
    Spring 2023
    HW5
    
    Brendan Sheehan

    This program provides a main menu function for the text
    editor functions.
'''

from text_editor import append
from text_editor import add
from text_editor import substitute
from text_editor import scramble
from text_editor import unscramble

def menu():
    print("Please select a letter from the following options.")
    print("a. Start with blank text.")
    print("b. Append to current text")
    print("c. Add text to current text at a specified position.")
    print("d. Substitute a word with another.")
    print("e. Scramble current text.")
    print("f. Unscramble current text.")
    print("g. Print current text.")
    print("h. Quit")
    
def main():

    new_text = ""
    current_text = ""
    # print menu of options and provide user input option
    menu()
    choice = input(str("Enter your choice here: "))

    # provide blank string for option a
    if choice == "a":
        current_text = ""

    #return to menu after a
    menu()
    choice = input(str("Youve chosen to start with blank text, what would you like to do next? "))

    # append after b
    elif choice == "b":
        new_text = input(str("Please enter the text you would like to append "))
        current_text = append(current_text, new_text)
        print("your new text is: ", current_text)

    # menu for new choice
    menu()
    choice = input(str("Enter your choice here"))

    # choice c add function
    elif choice == "c":
        new_text = input(str("Please enter the text you would like to add "))
        start = input(int("Please enter the number indicating the place you would like to add text "))
        current_text = add(current_text, new_text, start)
        print("Your new text is: ", current_text)

    # return to menu after c
    menu()
    choice = input(str("Enter your choice here"))

    # choice d substitute function
    elif choice == "d":

        word = input(str("Please enter the word you would like substituted"))
        new_word = input(str("Please enter the word you would like to substitute for your previous word"))
        current_text = substitute(current_text, word, new_word)
        print("Your new text is: ", current_text)

    # menu for new choice
    menu()
    choice = input(str("Enter your choice here"))

    # choice e scramble current text
    elif choice == "e":

        current_text = scramble(current_text)
        print("Your new text is: ", current_text)

    # menu for new choice
    menu()
    choice = input(str("Enter your choice here")

    # choice f unscramble current text
    elif choice == "f":
        current_text = unscramble(current_text)
        print("Your new text is: ", current_text)

    # menu for new choice
    menu()
    choice = input(str("Enter your choice here"))

    # choice g print current text
    elif choice == "g"
    print(current_text)

    # menu for new choice
    menu()
    choice = input(str("Enter your choice here")

        # response to selecting Quit
    else:
        if choice == "h":
        print("Thank you for using text editor, goodbye!")
                             
if __name__ == "__main__":
    main()
