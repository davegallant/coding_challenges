"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

"""

from typing import List


def get_powerset(nums: List[int]) -> List[List[int]]:
    """Iterative solution"""

    powerset = [[]]

    for num in nums:
        sets = []
        for i in powerset:
            sets += [i + [num]]
        powerset += sets
    return powerset


assert get_powerset(nums=[1, 2, 3]) == [
    [],
    [1],
    [2],
    [1, 2],
    [3],
    [1, 3],
    [2, 3],
    [1, 2, 3],
]


def get_powerset_recursive(nums: List[int]) -> List[List[int]]:

    if not nums:
        return [[]]

    prefix = get_powerset_recursive(nums[:-1])

    sets = []
    for pre in prefix:
        sets += [pre + [nums[-1]]]
    # sets = [pre + [nums[-1]] for pre in prefix]
    return prefix + sets


assert get_powerset_recursive(nums=[1, 2, 3]) == [
    [],
    [1],
    [2],
    [1, 2],
    [3],
    [1, 3],
    [2, 3],
    [1, 2, 3],
]
