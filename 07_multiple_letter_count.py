def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    freq_counter = {}

    for char in phrase:
        freq_counter[char] = (freq_counter.get(char) or 0) + 1

    return freq_counter