
def check_equal(a, b):
    value = None
    if a == b:
        value = a
    return value


def get_sum(a, b):
    equal = check_equal(a, b)
    if(check_equal(a, b) is not None):
        return equal

    largest = max(a, b) + 1
    smallest = min(a, b)
    sum = 0
    for x in range(smallest, largest):
        sum += x
    return sum


print(get_sum(1, 0))
print(get_sum(1, 2))
print(get_sum(0, 1))
print(get_sum(1, 1))
print(get_sum(-1, 0))
print(get_sum(-1, 2))
