#pangram if every letter is used at least once

def is_pangram(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if char not in s.lower():
            return False
    return True
