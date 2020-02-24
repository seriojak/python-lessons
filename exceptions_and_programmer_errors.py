import sys

DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def covert(s):
    """Convert a string to an integer"""
    x = -1
    try:
        number = ''

        for token in s:
            number += DIGIT_MAP[token]

        x = int(number)

    except (KeyError, TypeError):
        pass

    return x


print(covert(512))


def covert(s):
    """Convert a string to an integer"""
    x = -1
    try:
        number = ''

        for token in s:
            number += DIGIT_MAP[token]

        x = int(number)

    except (KeyError, TypeError) as e:
        print(f'Conversion error: {e!r}'),
        file = sys.stderr

    return x


print(covert(252))
