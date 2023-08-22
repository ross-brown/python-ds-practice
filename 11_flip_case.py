def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_phrase = ""
    lowered_to_swap = to_swap.lower()

    for char in phrase:
        if(char.lower() == lowered_to_swap):
            new_phrase += char.swapcase()
        else:
            new_phrase += char

    return new_phrase