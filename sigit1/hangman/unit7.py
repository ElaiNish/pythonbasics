def show_hidden_word(secret_word, old_letters_guessed):
    displayed_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()


def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True




