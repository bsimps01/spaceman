import random
import os

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open("/Users/benjamin5311/dev/MakeSchool/spaceman/words.txt", "r")
    words_list = f.readlines()
    f.close()

    #words_list = words_list[0.split('')]
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        #secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    for letters in secret_word:
        if letters in letters_guessed:
            return True
        else:
            return False
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    #pass

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
guesses_word
    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    pass


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''

    if secret_word.find(guess) > 0:
        return True
    else:
        return False
    #TODO: check if the letter guess is in the secret word

    pass




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    name = input("Enter your name: ")
    print("Welcome" + name + "to Spaceman! Try to guess each part of the word to win the game!")
    print("The correct word is {} letters long".format(len(secret_word)))
    print("You have {} incorrect guesses left".format(incorrect_guess))

    wordGuessed = False
    guesses_left = len(secret_word)
    letters_guessed = []
    guess = ""
    while True:
        guess = input("Enter a letter: ")
        if len(guess) != 1:
            return("Hold on there speed racer, one letter at time")
        else:
            pass
    while wrong_guessed > 0:
        print("Only {} guesses left, please enter one letter at a time".format(wrong_guessed))
        guess = input("Enter a letter: ")
    while len(guess) > 1:
        print("ONE letter at a time please")
        guess = input("Enter a letter: ")
    if is_guess_in_word(guess, secret_word) == False:
        if guess in letters_guessed:
            print("Too bad you already guessed that one, try again")
        else:
            letters_guessed.append(guess)
            print("Good Job")
            
    if is_word_guessed(secret_word,letters_guessed):
        print('Congratulations, you won!')
    elif guesses_left== 0:
        print ('Sorry, Game Over. The word was ' + secret_word)


    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost






#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)