"""
A sample encryption library using rot13.

"""

# File encoding PEP, see: http://legacy.python.org/dev/peps/pep-0263/
# -*- coding: utf-8 -*-

import re

def assign_and_return_positions(alphabet, rotation):
    """ This is an arbitrary rotation on a 26 character alphabet.

    """ 
    i = 0
    rotation_dict = dict()

    while i < len(alphabet):
        
        i_plus_rotation = (i + rotation) % len(alphabet)

        rotation_dict[alphabet[i]] = alphabet[i_plus_rotation]
        i += 1
    

    return rotation_dict


def apply_substitution(subst_dict, cleaned_string):
    """ Apply a substitution dictionary to a string.

    """
    encoded_string = ''

    # Slightly confusing, the get function will get the value of the
    # key named letter or will return letter.
    for letter in cleaned_string:
        encoded_string += subst_dict.get(letter, letter)
    
    return encoded_string


def clean_string(input_string):
    """ Reduce the input string to a-z.
    
    This is text munging. See the wikipedia article and python re docs.
    """
    allowed_chars = r'[^a-z .,;:\-_]'

    repl_char = '' # delete... will this work with None?

    return re.sub(allowed_chars,repl_char,input_string)


if __name__ == '__main__':
    """ Perform rotational encryption on an input.
    
    """
    
    alphabet = r'abcdefghijklmnopqrstuvwxyz'
    rotation = 13

    rotation_dict = assign_and_return_positions(alphabet, rotation)

    input_string = "Alphabet Soup; Acceptable Inputs: a-z, comma, period, colon, space, hyphen, underscore, and semicolon. Uppercase letters will be converted to lowercase."

    cleaned_input = clean_string(input_string.lower())
    
    print rotation_dict
    print cleaned_input

    encoded_input = apply_substitution(rotation_dict, cleaned_input)    

    print encoded_input

