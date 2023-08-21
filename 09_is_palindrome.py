def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    no_space_phrase = phrase.replace(" ", "")
    lowerd_phrase = no_space_phrase.lower()

    # letters = [char for char in lowerd_phrase]

    # letters.reverse()

    # reversed = ''.join(letters)

    # return reversed == lowerd_phrase

    start = 0
    end = len(lowerd_phrase) - 1

    while start < end:
        if not lowerd_phrase[start] == lowerd_phrase[end]:
            return False
        else:
            start += 1
            end -= 1
    return True
