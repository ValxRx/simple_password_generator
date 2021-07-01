from secrets import choice


def generate_password(length: int, special_chars: bool = None) -> str:
    """A function that generates a password given its length and optional special characters (not default)"""

    SOURCE_OF_LETTERS_WITHOUT_SPECIAL_CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                                               'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    SOURCE_OF_LETTERS_WITH_SPECIAL_CHARS = SOURCE_OF_LETTERS_WITHOUT_SPECIAL_CHARS + ["!", "@", "#", "$", "%", "^", "&", "*", "-", "_", "=", "+"]
    
    result = ''

    if special_chars:
        for _ in range(length):
            result += choice(SOURCE_OF_LETTERS_WITH_SPECIAL_CHARS)
    
    else:
        for _ in range(length):
            result += choice(SOURCE_OF_LETTERS_WITHOUT_SPECIAL_CHARS)
    
    return result


# Just a test
for i in range(10):
    print(f"Generated Password: {generate_password(12)}")
