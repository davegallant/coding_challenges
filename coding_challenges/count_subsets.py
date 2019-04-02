"""
[ 2, 4, 6, 10]

How many subsets of 16?

There are 2:
{ 6, 10 }
{ 2, 4, 10 }

Clarifying Questions
- Will there be negative integers? Only positive
- Assume the list is sorted? yes
- Are there any duplicates? No
= What if the sum of a subset is 16?

"""


def count_subsets(integers, desired_sum):
    return rec(integers, 0, desired_sum)


def rec(integers, current_sum, desired_sum):
    if current_sum > desired_sum:
        return 0
    if len(integers) == 0:
        if current_sum == desired_sum:
            return 1
        else:
            return 0
    return rec(integers[1:], current_sum + integers[0], desired_sum) + rec(
        integers[1:], current_sum, desired_sum
    )


assert count_subsets([2, 4, 6, 10], 16) == 2
assert count_subsets([2, 4, 6, 8, 10], 16) == 3
assert count_subsets([], 16) == 0
assert count_subsets([1, 2, 3, 4, 5], 7) == 3
assert count_subsets([1, 2], 3) == 1


# Now solve with dynamic programming / memoization


def count_subsets_memo(arr, desired_sum):
    return rec_memo(arr, desired_sum, len(arr) - 1, memo={})


def rec_memo(arr, total, i, memo):
    """Time complexity is o(n)"""
    key = f"{total}{i}"
    if key in memo:
        print("found key in memo. avoided recursion")
        print(f"{total}, {i}")
        return memo[f"{total}{i}"]
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif arr[i] > total:
        to_return = rec_memo(arr, total, i - 1, memo)
    else:
        to_return = rec_memo(arr, total - arr[i], i - 1, memo) + rec_memo(
            arr, total, i - 1, memo
        )
    memo[key] = to_return
    return to_return


assert count_subsets_memo([2, 4, 6, 10], 16) == 2
assert count_subsets_memo([2, 4, 6, 8, 10], 16) == 3
assert count_subsets_memo([], 16) == 0
assert count_subsets_memo([1, 2, 3, 4, 5], 7) == 3
assert count_subsets_memo([1, 2], 3) == 1
