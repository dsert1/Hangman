# Problem Set 2
# Name: Deniz Sert
# Collaborators: Frank Gonzalez
# Time spent: 5 hr
# Late Days used: 1

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    '''
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    '''
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    '''
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def check_victory(secret_word, letters_guessed):
    '''
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    '''

    
    #checks to see if there are no guesses
    if len(letters_guessed) == 0:
        return False
    if len(secret_word)== 0:
        return True
    #checks to see if there are any letters in the Secret Words not within
    #the list of guessed letters
    for x in secret_word:
        if x not in letters_guessed:
            return False
    return True



# Other tries
#    if secret_word==0:
#        return True
#    else:
#        if letters_guessed[0]==secret_word[0]:
#            secret_word
#
#

#    counter = 0
#    for x in range [0:letters_guessed]:
#        for y in range [0:letters_guessed]:
#            if letters_guessed[x]==secret_word[y]:
#                counter+=1
#    if counter==len(secret_word):
#        return True
#    return False
#    counter = 0
#    while (counter<len(letters_guessed)):
#        if letters_guessed[x] in secret_word:
#            counter+=1
#    if counter==len(secret_word):
#        return True
#    return False
##        
#        if letters_guessed[x] secret_word:
#            counter+=1
#    if counter==len(secret_word):
#        return True
#    return False
#
#    for x in range [0:letters_guessed]:
#        


def get_word_progress(secret_word, letters_guessed):
    '''
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and underscores (_) that represents
      which letters in secret_word have not been guessed so far
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guess = ""
    #checks to see if there are no guesses
    if len(letters_guessed) == 0:
        return "_"*len(secret_word)
    if len(secret_word)== 0:
        return ""
    #iterates through the Secret Word and concatenates the Guess string with
    #either a "_" or the letter
    for x in secret_word:
        if x in letters_guessed:
            guess+=x
        else:
            guess+="_"
    return guess
#str = "_"*secret_word.find(x)+"_"*(len(secret_word)-secret_word.index(0))

def get_remaining_letters(letters_guessed):
    '''
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #sets up the string to print (contain null)
    str = ""
    #checks to see if there are no guesses
    if len(letters_guessed) == 0:
        return string.ascii_lowercase
    #iterates through all letters to see if it is in the letters_guessed list
    #if a letter has been guessed already, it is not added to str
    for x in string.ascii_lowercase:
        if x in letters_guessed:
            pass
        else:
            str+=x
    return str
            


def hangman(secret_word_):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    #initiates game and welcomes user
    num_guesses = 10
    print("Welcome to Hangman!")
    print("I am thinking of a word that is", len(secret_word_), "letters long.")
    print("--------------")
    
    #computer chooses a words


    letters_guessed = []


    while(num_guesses>0):
        #informs player on number of guesses left
        print("You have", num_guesses, "guesses left.")
        print("Available letters:", get_remaining_letters(letters_guessed))
        
        #user enters guess
        guess = input("Please guess a letter: ")
        guess = str.lower(guess)

        #game handles it if a special character was inputted
        if str.isalpha(guess) is False:
            print("That is not a valid letter. Please enter an input from the alphabet:")
        elif (guess in letters_guessed):
            print("Oops! You've already guessed that letter:", get_word_progress(secret_word_, letters_guessed))
        
        # incorrect guess
        elif (guess not in secret_word_):
            letters_guessed.append(guess)
            print("Oops! That letter is not in my word:", get_word_progress(secret_word_, letters_guessed))
            num_guesses-=1
        # correct guess
        else:
            letters_guessed.append(guess)
            print("Good guess:", get_word_progress(secret_word_, letters_guessed))

        #ran out of guesses
        
        print("--------------")
        if num_guesses<=0:
            print("Sorry, you ran out of guesses. The word was " + secret_word_)
            break
        elif check_victory(secret_word_, letters_guessed):
            print("Congratulations, you won!")



            # finds num of unique characters in the Secret Word
            unique = []

            for x in secret_word_:
                if x in unique:
                    pass
                else:
                    unique.append(x)

            #computes score
            print("Your total score for this game was", (2 * (num_guesses) + 3 * (len(secret_word_) + len(unique))))
            break

    


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

# -----------------------------------

def choose_letter(secret_word, letters_guessed):
    '''
    * Chooses a random letter to help the player
    
    
    '''
    l = []
    for x in secret_word:
        if x in letters_guessed:
            pass
        else:
            l.append(x)
    new = random.randint(0, len(l)-1)
    revealed_letter = l[new]
    
    return revealed_letter
    
def hangman_with_help(secret_word_):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make sure that
      the user puts in a letter.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 2 guesses. If the user does
      not have 2 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    num_guesses = 10

    #initialize game
    print("Welcome to Hangman!")
    print("I am thinking of a word that is", len(secret_word_), "letters long.")
    print("--------------")
    


    letters_guessed = []
    hint = ""
    called_out = False

    while(num_guesses>0):
        #inform player on number of guesses
        print("You have", num_guesses, "guesses left.")
        print("Available letters:", get_remaining_letters(letters_guessed))
        
        #user guesses
        guess = input("Please guess a letter: ")
        guess = str.lower(guess)
        if str.isalpha(guess) is False:
            #hint
            if guess == "!":
                if num_guesses<=2:
                    print("Oops! Not enough guesses left!", get_word_progress(secret_word_, letters_guessed))
                else:
                    hint = choose_letter(secret_word_, letters_guessed)
                    print("Letter revealed: ", hint)
                    letters_guessed+=hint
                    num_guesses-=2
                    print(get_word_progress(secret_word_, letters_guessed))
                    #yeet
            #special character (not hint)
            else:
                print("Oops! That is not a valid letter. Please input a letter from the alphabet", get_word_progress(secret_word_, letters_guessed))
                called_out = True

        #already guessed letter
        if (guess in letters_guessed):
            if (hint in letters_guessed):
                pass
            else:
                print("Oops! You've already guessed that letter:", get_word_progress(secret_word_, letters_guessed))

        #handles if hint was given and incorrect guess
        elif (guess not in secret_word_):
            if (hint in letters_guessed):
                pass
            else:
                if called_out is True:
                    pass
                else:
                    letters_guessed.append(guess)
                    print("Oops! That letter is not in my word:", get_word_progress(secret_word_, letters_guessed))
                    num_guesses -= 1
        #correct guess
        else:
            letters_guessed.append(guess)
            print("Good guess:", get_word_progress(secret_word_, letters_guessed))

        print("--------------")
        #ran out of guesses
        if num_guesses <= 0:
            print("Sorry, you ran out of guesses. The word was " + secret_word_)
            break
        #win
        elif check_victory(secret_word_, letters_guessed):
            print("Congratulations, you won!")

            # finds num of unique characters in the Secret Word
            unique = []

            for x in secret_word_:
                if x in unique:
                    pass
                else:
                    unique.append(x)

            #prints score
            print("Your total score for this game was", (2 * (num_guesses) + 3 * (len(secret_word_) + len(unique))))
            break


# When you've completed your hangman_with_help function, comment the two similar
# lines below that were used to run the hangman function, and then uncomment
# those two lines and run this file to test!

# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # To test part 2, uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman("ab")

###############

    # To test part 3, comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_help(secret_word)

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.

