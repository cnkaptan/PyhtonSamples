fhand = open("mbox-short.txt", "r")  # open(filename,mode) modes = open, read,write,close
# read r
# write w
# open(filename) read modda acilir
print fhand
count = 0
# fhand deki her bor satir bir string seklinde okur
# for cheese in fhand:
#     count+=1
#     print cheese, #her satir zaten \n le bittigi icin printte \n koyuyor o yuzden oldugu gibi yazdirmak icin virgulle devam ettik

# inp = fhand.read()
# print len(inp)
#
# print inp[:20]


# for line in fhand:
#     line = line.strip()
#     if line.startswith("From"):
#         print line

# for line in fhand:
#     line = line.strip()
#     if not line.startswith("From"):
#         continue
#     print line

# for line in fhand:
#     line = line.strip()
#     if not "@uct.ac.za" in line:
#         continue
#     print line

# fname = raw_input("Enter the fila name: ")
#
# try:
#     fhand = open(fname)
# except:
#     print "File cannot be opened:",fname
#     exit()
#
# count = 0
# for line in fhand:
#     if line.startswith("Subject:"):
#         count+=1
# print "There were ", count, "subject line in ", fname


# fname = raw_input("Enter file name: ")
fh = open("mbox-short.txt")
count = 0
average = 0.0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        average += float(line.split(":")[1])
        count += 1
print average/count
