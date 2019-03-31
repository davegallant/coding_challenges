"""
Given a string of digits, calculate the number of ways they can
be represented.
1 -> a
2 -> b
3 -> c
...
26 -> z

Examples:

"1234" -> abcd, lcd, awd -> 3 ways
"12" -> 2 ways
"33" -> 1 way

Edge cases:
"0123" -> 0 ways


Assumptions:
- All characters are digits than less 10
"""


def helper(data, k, memo):
    """Use recursion, and memoization to save computations."""
    if k == 0:
        return 1
    i = len(data) - k
    if data[i] == "0":
        return 0
    if memo.get(k):
        return memo[k]
    result = helper(data, k - 1, memo)
    if k >= 2 and int(data[i : i + 2]) <= 26:
        result += helper(data, k - 2, memo)
    memo[k] = result
    return result


def num_ways(data):
    if data[0] == 0:
        return 0
    return helper(data, k=len(data), memo={})


assert num_ways("12345") == 3
assert num_ways("27345") == 1
assert num_ways("324") == 2
assert num_ways("3234") == 2
assert num_ways("32340") == 0
assert num_ways("012") == 0

# worst case (hence the need for memoization)
assert num_ways("111111") == 13
