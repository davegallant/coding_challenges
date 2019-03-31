"""
Given an array of integers, determine whether there is a pair
of integers that can match a particular sum.

Assumptions:
List is sorted.
Sum wanted is always an integer.
"""


def has_pair_with_sum(given_array, sum_wanted):
    left_marker = 0
    right_marker = len(given_array) - 1

    while left_marker < right_marker:
        if given_array[left_marker] + given_array[right_marker] == sum_wanted:
            return True
        if given_array[left_marker] + given_array[right_marker] < sum_wanted:
            left_marker += 1
        else:
            right_marker -= 1
    return False


assert has_pair_with_sum([1, 2, 3, 9, 12], sum_wanted=5) == True
assert has_pair_with_sum([1, 2, 3, 9, 12], sum_wanted=5) == True
assert has_pair_with_sum([], sum_wanted=6) == False


# Now assume that the given array of integers is unsorted:


def has_pair_with_sum_unsorted(given_array, sum_wanted):
    complements = set()
    for number in given_array:
        if number in complements:
            return True
        complements.add(sum_wanted - number)
    return False


assert has_pair_with_sum_unsorted([3, 2, 9, 5], sum_wanted=7) == True
assert has_pair_with_sum_unsorted([3, 2, 9, 6], sum_wanted=7) == False
