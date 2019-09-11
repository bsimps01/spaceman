import random


def load_word():
    
    with open('/Users/benjamin5311/dev/MakeSchool/spaceman/words.txt', 'r') as f:
        words_list = f.read().split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(letters_guessed):
    if not '_' in letters_guessed:
        return True
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    #pass

def get_guessed_word(secret_word, letters_guessed):
    print("letters_guessed " + str(letters_guessed))
    
    word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            word += letter
        else:
            word += "_"
    return word

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    #pass


def is_guess_in_word(guess, secret_word, letters_guessed):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''

    if guess.isalpha() == False:
        print("Enter a letter here ")
    elif len(guess) > 1:
        print("Choose one at a time speedy")
    elif guess in letters_guessed:
        print("Too bad you already guessed that one, try again ")
        print(letters_guessed)
    elif guess in secret_word:
        letters_guessed.append(guess)
        #"".join(letters_guessed)
        return True
    else:
        letters_guessed.append(guess)
        return False
    #TODO: check if the letter guess is in the secret word

    #pass




def spaceman(secret_word):
    
    correct = "Good Guess "
    wrong = 0
    did_you = "_"
    woops = "Wrong Answer, Current guesses left: "
    letters_guessed = []
    #remaining_guesses = len(secret_word)

    name = input("Enter your name: ")
    print("Welcome " + name + " to Spaceman! Try to guess each part of the word to win the game!")
    print("The correct word is {} letters long".format(len(secret_word)))

    for guesses in range(30):
        guesses += 1
        guess = input('Enter a letter: ').lower()
        a = is_guess_in_word(guess, secret_word, letters_guessed)
        if a:
            did_you = get_guessed_word(secret_word,letters_guessed)
            print(correct + did_you)
            if is_word_guessed(did_you):
                success = "Congrats! You won!"
                print(success)
                print("Your word was " + secret_word )
                break
        elif a == False:
            if wrong == 7:
                loss = "Sorry, Game Over homie. Now you are a SPACEMAN!"
                print(loss)
                print ('The word was ' + secret_word)
                break
            #elif remaining_guesses == 0:
                
            else:
                wrong += 1
                losing = 8 - wrong
                print(woops + str(losing))

    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost






#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)