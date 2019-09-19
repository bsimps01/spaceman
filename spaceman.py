import random


def load_word():
    
    with open('/Users/benjamin5311/dev/MakeSchool/spaceman/words.txt', 'r') as f:
        words_list = f.read().split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(letters_guessed):
    if not '_' in letters_guessed:
        return True

def test_is_word_guessed():
    assert is_word_guessed("good") == True
    assert is_word_guessed("r3jected") == False
    assert is_word_guessed("great") == True

def get_guessed_word(secret_word, letters_guessed):
    print("letters_guessed " + str(letters_guessed))
    
    word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            word += letter
        else:
            word += "_"
    return word

def test_get_guessed_word():
    assert get_guessed_word(("fun"), ["f","u"]) == "fu_"
    assert get_guessed_word(("weird"), ["w","e","r","d"]) == "we_rd"
    assert get_guessed_word(("puppy"), ["p","u","p","p","y"]) == "puppy"

def is_guess_in_word(guess, secret_word, letters_guessed):

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

def test_is_guess_in_word(is_guess_in_word):
    assert is_guess_in_word(("h", "o", "m", "e"), ("home")) == True
    assert is_guess_in_word(("b", "a", "s", "e"), ("base")) == True
    assert is_guess_in_word(("w", "a", "s", "h"), ("wash")) == True
    assert is_guess_in_word(("g", "r", "e", "a", "t"), ("great")) == True


def spaceman(secret_word):
    
    correct = "Good Guess "
    wrong = 0
    did_you = "_"
    woops = "Wrong Answer, Current guesses left: "
    letters_guessed = []

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
                
            else:
                wrong += 1
                losing = 8 - wrong
                print(woops + str(losing))

if __name__ == "__main__":
    test_is_word_guessed()
    test_get_guessed_word()
    test_is_guess_in_word(is_guess_in_word)
#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)