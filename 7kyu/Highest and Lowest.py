# DESCRIPTION:
# In this little assignment you are given a string of space separated numbers, and have to return the
# highest and lowest number.


def high_and_low(numbers):
    numbers_s = sorted(numbers.split(), key=int)
    numbers = f'{numbers_s[-1]} {numbers_s[0]}'
    return numbers
