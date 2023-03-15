def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    rev_value = value.lower()[::-1]
    val_2 = value.lower()

    if val_2.replace(" ", "") == rev_value.replace(" ", "") :
        return True
    else :
        return False
