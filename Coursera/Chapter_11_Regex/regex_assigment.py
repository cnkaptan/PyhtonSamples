import re

handle = open("regex_sum_195270.txt", "r")
str = handle.read()
k = 0
for num in re.findall(r"[0-9]+", str):
    k += int(num)

print k

print sum([int(number) for number in re.findall(r"[0-9]+", open("regex_sum_195270.txt", "r").read())])

print sum(list(map(lambda x: int(x),re.findall(r"[0-9]+", open("regex_sum_195270.txt", "r").read()))))