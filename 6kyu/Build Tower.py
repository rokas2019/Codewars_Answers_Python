# Build Tower Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A
# tower block is represented with "*" character.
#
# For example, a tower with 3 floors looks like this:

def tower_builder(n):
    return [('*' * i).center(n * 2 - 1) for i in range(1, 2 * n + 1, 2)]