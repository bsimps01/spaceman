from spaceman import *

def test_is_guess_in_word():
    secret_word = ["b", "u", "s", "h"]
    assert is_guess_in_word("s", secret_word) == True, "Guess in word not finding character"
    assert is_guess_in_word("v", secret_word) == False, "Returing other than false on incorrect test"

def test_is_word_guessed():
    letters_guessed = ["d", "o", "g"]
    secret_word = "dog"
    assert is_word_guessed(secret_word, letters_guessed) == True, "is_word_guessed function not working"
    letters_guessed = ["d", "o", "g"]
    assert is_word_guessed(secret_word, letters_guessed) == False, "Doesn't return false on incorrect guess"

def test_get_guessed_word():
    # Test setup
    secret_word = ["d", "o", "g"]
    letters_guess_so_far = ["d", "g"]

    # Test to make sure it works
    assert get_guessed_word(
        secret_word, letters_guess_so_far) == "d_g", "returning correct statement"
    # Test incorrect
    assert get_guessed_word(
        secret_word, letters_guess_so_far) != "__g", "Returning incorrect string"