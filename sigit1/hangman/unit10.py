HANGMAN_ASCII_ART="""
    Welcome to the game Hangman
      _    _
     | |  | |
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |
                         |___/
"""
MAX_TRIES =6


HANGMAN_PHOTOS = {
    1: """
       x-------x""",
    2: """
       x-------x
       |
       |
       |
       |
       |
    """,
    3: """"
       x-------x
       |       |
       |       0
       |
       |
       |""",
    4: """
       x-------x
       |       |
       |       0
       |       |
       |
       |""",
    5: """ 
       x-------x
       |       |
       |       0
       |      /|\\
       |
       |""",
    6: """
       x-------x
       |       |
       |       0
       |      /|\\
       |      /
       |""",
    7: """
        x-------x
       |       |
       |       0
       |      /|\\
       |      / \\
       |"""

}

def is_valid_input(letter):
    """
    Check if the given input is a valid character (a single English letter)

    Args:
    letter_guessed (str): the string to be checked

    Returns:
    bool: True if the input is a valid character, False otherwise
    """
    letter=letter.lower()
    # Check if the input string has length > 1
    if len(letter) != 1:
        return False
    # Check if the input string contains non-alphabetic characters
    if not letter.isalpha():
        return False
    if not(letter>='a' and letter<='z'):
        return False

    return True

def check_valid_input(letter_guessed, old_letters_guessed):
    if not is_valid_input(letter_guessed):
        return False

    if letter_guessed.lower() in [x.lower() for x in old_letters_guessed]:
        return False

    # The input string is a valid guess
    return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print("X")
        print(" -> ".join(sorted([x.lower() for x in old_letters_guessed])))
        return False


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

def print_hangman(num_of_tries):
    if num_of_tries in range(0, 7):
        print(HANGMAN_PHOTOS[num_of_tries])
    else:
        print("invalid number of guesses")

def choose_word(file_path, index):
    with open(file_path, 'r') as f:
        words = f.read().split()
        unique_words = set(words)
        num_unique_words = len(unique_words)
        word_index = (index - 1) % len(words)
        return (num_unique_words, words[word_index])

def print_welcome_screen():
    print(HANGMAN_ASCII_ART, MAX_TRIES)


def main():
    print_welcome_screen()
    old_letters_guessed = []
    num_of_tries = 0
    file_path = input("Enter file path: ")
    word_index = int(input("Enter index: "))
    print("Let’s start!")
    p, secret_word = choose_word(file_path, word_index)
    print_hangman(num_of_tries)
    print(show_hidden_word(secret_word, old_letters_guessed))
    won = False
    while num_of_tries < MAX_TRIES and not won:
        letter_guessed = input("Guess a letter: ")
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            if letter_guessed.lower() in secret_word:
                won = check_win(secret_word, old_letters_guessed)
            else:
                num_of_tries += 1
                print_hangman(num_of_tries)
            print(show_hidden_word(secret_word, old_letters_guessed))

    if won:
        print("won")
    else:
        print("loss")


if __name__ == '__main__':
    main()
