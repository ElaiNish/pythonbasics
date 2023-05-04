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



if __name__ == '__main__':
    old_letters = ['a', 'p', 'c', 'f']
    print(try_update_letter_guessed('A', old_letters))
