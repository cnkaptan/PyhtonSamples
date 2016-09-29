def get_ratios(L1, L2):
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index] / float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN'))  # NaN = Not a Number
        except:
            raise ValueError('get_ratios called with a bad arg')
    return ratios


L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 0]
L3 = [7, 8, 9]


# print(get_ratios(L1, L2))
# print(get_ratios(L1, L3))

# def fancy_divide(numbers, index):
#     try:
#         denom = numbers[index]
#         for i in range(len(numbers)):
#             numbers[i] /= denom
#     except IndexError:
#         print("-1")
#     else:
#         print("1")
#     finally:
#         print("0")

# def fancy_divide(numbers, index):
#     try:
#         denom = numbers[index]
#         for i in range(len(numbers)):
#             numbers[i] /= denom
#     except IndexError:
#         fancy_divide(numbers, len(numbers) - 1)
#     except ZeroDivisionError:
#         print("-2", end=",")
#     else:
#         print("1", end=",")
#     finally:
#         print("0", end=",")
#     print()

def fancy_divide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            fancy_divide(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        print("-2")


# fancy_divide([0, 2, 4], 1)
# fancy_divide([0, 2, 4], 4)
# fancy_divide([0, 2, 4], 0)
