# DESCRIPTION: Implement the function unique_in_order which takes as argument a sequence and returns a list of items
# without any elements with the same value next to each other and preserving the original order of elements.


def unique_in_order(sequence):
    chars = []
    for i in range(len(sequence)):
        if i == 0 or sequence[i] != sequence[i - 1]:
            chars.append(sequence[i])
    return chars