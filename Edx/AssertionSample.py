def avg(grades):
    assert not len(grades) == 0  # no grades data
    return sum(grades) / len(grades)


# print(avg([1, 2, 3, 4, 5]))
# print(avg([]))

def normalize(numbers):
    max_number = max(numbers)
    assert (max_number != 0), "Cannot divide by 0"
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
        assert (0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
    return numbers


try:
    normalize([0, 0, 0])
except ZeroDivisionError:
    print('Invalid maximum element')
