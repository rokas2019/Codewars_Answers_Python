# Take an array and remove every second element from the array. Always keep the first element and start removing with
# the next element.
#
# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
#
# None of the arrays will be empty, so you don't have to worry about that!

def remove_every_other(my_list):
    return my_list[::2]


def remove_every_other_2(my_list):
    lst_k = []
    for i in range(len(my_list)):
        if i == 0 or i % 2 == 0:
            lst_k.append(my_list[i])
    return lst_k




