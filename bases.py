#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def split(digits):
    if len(digits) > 0:
        return [char for char in digits]
    else:
        return digits


def convert_to_alpha(digit):
    digit_dict = {
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17,
        'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25,
        'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33,
        'Y': 34, 'Z': 35
    }

    if digit.isalpha():
        digit = digit.upper()
        digit = digit_dict[digit]
        return digit
    elif digit.isnum():
        return digit
    else:
        print("ERROR: Invalid Character")


def make_digit_list(digits):
    '''convert digits of non-decimal numeric base systems to a list of
    decimals'''
    # get digits string and split each charater
    digit_list = split(digits)
    # reverse the order of the list so last digit is first
    digit_list.reverse()

    digit_dict = {
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17,
        'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25,
        'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33,
        'Y': 34, 'Z': 35
    }

    print('')
    print('digits in digit_list:')
    index_tracker = 0
    for digit in digit_list:

        digit = digit.rstrip()
        print('checking for alpha digits')
        if digit.isalpha():
            print('alpha digit identified')
            # convert alpha list item to upper case
            digit = digit.upper()
            print(digit)
            if digit in digit_dict:
                # assign value from corresponding dict key
                digit = digit_dict.get(digit)
                print('alpha digit converted to decimal numeric: ', digit)
                digit_list[index_tracker] = digit
            else:
                print('invalid char: ' + str(digit))
        index_tracker += 1

    return digit_list


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    digit_list = make_digit_list(digits)

    # split digits into a list of digits
    number_of_digits = len(digit_list)
    # get length of list of digits
    range_limit = int(number_of_digits)
    print("range_limit= ", range_limit)
    print("digit_list=", digit_list)
    # set range limit
    converted_decimal = 0
    # begin summing with last digit of digits (recall list was reversed by
    #   make_digit_list helper function)
    for i in range(0, range_limit):
        # steps through range of exponents which are the same as the list index
        if str(digit_list[i]).isalpha():
            print("The digit " + str(digit_list[i]) + " is a letter.")
        else:
            print('the converted decimal is ', (int(digit_list[i]) * (base ** i)))
            converted_decimal += (int(digit_list[i]) * (base ** i))
    return converted_decimal


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    # ...
    # TODO: Encode number in hexadecimal (base 16)
    # ...
    # TODO: Encode number in any base (2 up to 36)
    # ...
    encoded_digits_list = []
    while number > 0:
        new_digit = number % base
        number = number - (number // base)
        encoded_digits_list.prepend(new_digit)
    for digit in encoded_digits_list:
        if digit > 9:
            digit.convert_to_alpha()
        encoded_number += str(digit)
    return encoded_number


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    # import sys
    # args = sys.argv[1:]  # Ignore script file name
    # if len(args) == 3:
    #     digits = args[0]
    #     base1 = int(args[1])
    #     base2 = int(args[2])
    #     # Convert given digits between bases
    #     result = convert(digits, base1, base2)
    #     print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    # else:
    #     print('Usage: {} digits base1 base2'.format(sys.argv[0]))
    #     print('Converts digits from base1 to base2')
    print(decode('a', 16))

if __name__ == '__main__':
    main()
