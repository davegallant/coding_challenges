sert (
    num_ways(height=4, step_sizes=[1, 3, 5])
    == 3
    == num_ways_bottom_up(height=4, step_sizes=[1, 3, 5])
)

assert (
    num_ways(height=4, step_sizes=[1, 2, 3])
    == 7
    == num_ways_bottom_up(height=4, step_sizes=[1, 2, 3])
)
