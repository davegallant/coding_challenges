"""
Add one to a list of integers.
Any integer cannot be more than 10.
"""


def add_one(given_array):
    """add one to an array"""
    result = [None] * len(given_array)
    carry = 1
    for i in range(len(given_array), 0, -1):
        sum = given_array[i - 1] + carry
        if sum == 10:
            carry = 1
        else:
            carry = 0
        result[i - 1] = sum % 10
    if carry == 1:
        result = [1] + result
    return result


assert add_one([2]) == [3]
assert add_one([2, 9]) == [3, 0]
assert add_one([9]) == [1, 0]
assert add_one([9, 9, 9]) == [1, 0, 0, 0]

# This solution does not consider negative numbers!
# assert add_one([-3]) == [-2]
