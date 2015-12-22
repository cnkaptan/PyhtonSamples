# for i in [1, 2, 3, 4, 5]:
#     print i
# print "Blastoff!"
#
# friends = ["Joseph", "Glenn", "Sally"]
# for friend in friends:
#     print "Happy New Year: ", friend
# print "Done!"
#
# largest_so_far = -1
# print "Before ", largest_so_far
# for the_num in [9, 41, 12, 3, 74, 15]:
#     if the_num > largest_so_far:
#         largest_so_far = the_num
#     print largest_so_far, "\t", the_num
# print "After ", largest_so_far
#
# zork = 0
# print "Before ", zork
#
# for thing in [9, 41, 12, 3, 74, 15]:
#     zork += thing
#     print zork, thing
# print "After", zork
#
# count = 0
# sum = 0
# print "Before", count, sum
# for value in [9, 41, 12, 3, 74, 15]:
#     count += 1
#     sum += value
#     print count, sum, value
# print "After", count, sum, sum / count
#
largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    try:
        if num == "done":
            break
        fNum = float(num)
        if smallest is None:
            smallest = fNum
        if largest is None:
            largest = fNum
        elif fNum < smallest:
            smallest = fNum
        elif fNum > largest:
            largest = fNum
    except:
        print "Invalid input"

print "Maximum", largest
print "Minimum", smallest