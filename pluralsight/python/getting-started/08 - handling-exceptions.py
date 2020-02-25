print('-' * 15 + 'Handling Exceptions' + '-' * 15)

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
    number = ''

    for token in s:
        number += DIGIT_MAP[token]

    x = int(number)

    return x


print(covert("one three three seven".split()))


# print(covert("around two billion".split()))

def covert(s):
    try:
        number = ''

        for token in s:
            number += DIGIT_MAP[token]

        x = int(number)
        print(f"Conversion succeeded!")
    except KeyError:
        print(f"Conversion failed!")
        x = -1

    return x


print(covert("around two billion".split()))


# print(covert(512))

def covert(s):
    """Convert a string to an integer"""
    try:
        number = ''

        for token in s:
            number += DIGIT_MAP[token]

        x = int(number)
        print(f"Conversion succeeded!")

    except KeyError:
        print(f"Conversion failed!")
        x = -1

    except TypeError:
        print(f"Conversion failed!")
        x = -1

    return x


print(covert(512))


# print(covert(512))

def covert(s):
    """Convert a string to an integer"""
    x = -1
    try:
        number = ''

        for token in s:
            number += DIGIT_MAP[token]

        x = int(number)
        print(f"Conversion succeeded!")

    except (KeyError, TypeError):
        print(f"Conversion failed!")

    return x


print(covert(512))
