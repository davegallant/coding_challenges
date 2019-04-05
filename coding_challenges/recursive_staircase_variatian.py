"""
There is a staircase with number of steps height.

You can take any size step in an array (i.e x=[1,3,5])

How many ways can you reach to the top of the stairs?

"""


def num_ways(height, step_sizes):
    """Use recursion."""
    result = 0
    if height == 0:
        return 1
    for step_size in step_sizes:
        if height >= step_size:
            result += num_ways(height - step_size, step_sizes)
    return result


def num_ways_bottom_up(height, step_sizes):
    """Use an iterative approach."""
    ways = {}
    if height == 0:
        return 1
    ways[0] = 1
    for current_height in range(1, height + 1):
        total = 0
        for step_size in step_sizes:
            if current_height >= step_size:
                total += ways[current_height - step_size]
        ways[current_height] = total
    return ways[height]


assert (
    num_ways(height=4, step_sizes=[1, 3, 5])
    == 3
    == num_ways_bottom_up(height=4, step_sizes=[1, 3, 5])
)

assert (
    num_ways(height=4, step_sizes=[1, 2, 3])
    == 7
    == num_ways_bottom_up(height=4, step_sizes=[1, 2, 3])
)
