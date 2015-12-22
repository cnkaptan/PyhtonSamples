import re

hand = open("/Users/cnkaptan/PycharmProjects/PyhtonSamples/Coursera/mbox-short.txt")

# for line in hand:
#     line = line.strip()
#     if re.search("From:", line):
#         print line


# for line in hand:
#     line = line.strip()
#     # sapka karakteri orda satirin basina gore arama yapmasini sagliyor
#     if re.search("^From:", line):
#         print line



# for line in hand:
#     line = line.strip()
#     # aradki iki nokta bize oralara herhangi bir karakteri gelebilecigni temsil ediyor
#     if re.search("F..m:", line):
#         print line

# for line in hand:
#     line = line.strip()
#     if re.search("From:.+@", line):
#         print line

# s = 'Hello from csev@umich.edu to cwen@iupui.edu about the meeting @2PM'
# lst = re.findall("\S+@\S+",s) # findall method string listesi doner
#
# print lst


# for line in hand:
#     line = line.strip()
#     if re.search("^X-\S+", line):
#         print line

# x = "My 2 favourite numbers are 19 and 42"
# y = re.findall("[0-9]+", x)
# print y

# x = "From: Using the : character"
# y = re.findall("^F.+:", x)
# print y

# x = "From: Using the : character"
# y = re.findall("^F.+?:", x)
# print y

# x = "From: cihan-kaptan@outlook.com Sat Jan 5 09:14:16 2008"
# # y = re.findall("\S+@\S+", x)
# y = re.findall("^From:.*? (\S+@\S+)", x)
# print y


# data = "From cihan-kaptan@outlook.com Sat Jan 5 09:14:16 2008"
#
# atpos = data.find("@")
# print atpos

# atpos yani 18inci indexten basla
# sppos = data.find(" ", atpos)
# print sppos
#
# host = data[atpos + 1:sppos]
# print host
#
# words = data.split()
# email = words[1]
# pieces = email.split("@")
# print pieces[1]

# y = re.findall("@([^ ]*)", data)
# print y


# y = re.findall("^From .*@([^ ]*)", data)
# print y

# numlist = list()
# for line in hand:
#     line = line.strip()
#     stuff = re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line)
#     if len(stuff) != 1:
#         continue
#     num = float(stuff[0])
#     numlist.append(num)
# print "Maximum:", max(numlist)


x = "We just received $10.00 for cookies."
y = re.findall("\$[0-9.]+", x)
print y
