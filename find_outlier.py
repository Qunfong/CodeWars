# My solution

# Checks if the pattern is odd or even.


def find_pattern(integers):
    odd_or_even = False
    odd = []
    even = []
    for integer in integers:
        if integer % 2 == 0:
            even.append(integer)
        else:
            odd.append(integer)

    if len(even) >= 2:
        odd_or_even = True
    return odd_or_even

# Loop trough array and checking if integer is an anomaly


def loop_with_modulo(integers, even):
    for integer in integers:
        if(integer % 2 == even):
            return integer

# Find outlier in array of either even or odd integers with array size of 3 or greater.


def find_outlier(integers):
    outlier = None
    even = find_pattern(integers[:3])  # Check odd or even
    # find anomaly in array of odd/even.
    outlier = loop_with_modulo(integers, even)
    return outlier

# Best solution found on codewars
# We also see that the running time is n
# This is better than my solution because
# 1.It's more compact/easier
# 2.In my mind my running time would be o(3) + o(n), and this solution is o(n) + o(n) which is the same
# when array would be nearly infinite.


def find_outlier2(int):
    odds = [x for x in int if x % 2 != 0]
    evens = [x for x in int if x % 2 == 0]
    return odds[0] if len(odds) < len(evens) else evens[0]


print(find_outlier2([160, 3, 1719, 19, 11, 13, -21]))
