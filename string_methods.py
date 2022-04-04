import random
import string


def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def chars_count(rand_string):
    chars_data = {'letters': 0, 'numbers': 0}
    for symbol in rand_string:
        if symbol.isalpha():
            chars_data['letters'] += 1
        elif symbol.isdigit():
            chars_data['numbers'] += 1

    return chars_data
