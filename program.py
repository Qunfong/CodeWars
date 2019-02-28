# Find the irregular element in a list. This can be either an even series or uneven series which has a single occurence of the opposite.
def iq_test(numbers):
    numbers = list(map(int, numbers.split(" ")))
    odd = []
    even = []

    for i in range(len(numbers[0:])):
        if numbers[i] % 2 == 0:
            even.append(i+1)
        else:
            odd.append(i+1)
        if (len(odd) > 1 and len(even) >= 1) or (len(odd) >= 1 and len(even) > 1):
            if len(odd) == 1:
                return odd[0]
            else:
                return even[0]


iq_test("4 3 7 49")
