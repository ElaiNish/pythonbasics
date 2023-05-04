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



if __name__ == '__main__':
    print(is_valid_input('ab'))