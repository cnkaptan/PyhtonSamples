fName = raw_input("Enter file name: ")
if len(fName) < 1:
    fName = "mbox-short.txt"
fh = open(fName)
lst = list()
for line in fh:
    if line.startswith("From "):
        email = line.split()[1]
        lst.append(email)
        print email
count = len(lst)
print "There were", count, "lines in the file with From as the first word"