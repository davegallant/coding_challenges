"""
There is a staircase with number of steps height.

You can take either a single step or a double.

How many ways can you reach to the top of the stairs?

"""


def num_ways(height):
    """Use recursion"""
    if height == 0 or height == 1:
        return 1
    return num_ways(height - 1) + num_ways(height - 2)


def num_ways_bottom_up(height):
    """Use iteration"""
    ways = {}
    if height == 0 or height == 1:
        return 1
    ways[0] = 1
    ways[1] = 1
    for i in range(2, height + 1):
        ways[i] = ways[i - 1] + ways[i - 2]
    return ways[height]


assert num_ways(0) == 1 == num_ways_bottom_up(0)
assert num_ways(1) == 1 == num_ways_bottom_up(1)
assert num_ways(2) == 2 == num_ways_bottom_up(2)
assert num_ways(3) == 3 == num_ways_bottom_up(3)
assert num_ways(4) == 5 == num_ways_bottom_up(4)
assert num_ways(5) == 8 == num_ways_bottom_up(5)

# Spoiler, this is fibonacci
