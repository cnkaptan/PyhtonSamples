n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print n

# index aliyor ve o indexteki elemani donuyor
num1 = n.pop(2)
print num1
print n

#eleman aliyor ve geriye eleman donmuyor
num2 = n.remove(4)
print num2
print n

# o indexteki elemani siliyor
del n[4]
print n


m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!
def join_lists(x,y):
    return x + y


print join_lists(m, n)
# You want this to print [1, 2, 3, 4, 5, 6]


n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
    results = []
    for numbers in lists:
        for num in numbers:
            results.append(num)
    return results


print flatten(n)