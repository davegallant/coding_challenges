"""
Given a string, get the first recurring character.

Examples:

abcdea -> a
ddd -> d

Edges cases:

abc -> None
-> None
"""


def get_first_recurring_char(given_array):
    occurences = set()
    for char in given_array:
        if char in occurences:
            return char
        occurences.add(char)


assert get_first_recurring_char("abcdab") == "a"
assert get_first_recurring_char("bbbb") == "b"
assert get_first_recurring_char("abc") == None
assert get_first_recurring_char("") == None

