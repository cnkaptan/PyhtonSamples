name = raw_input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

ddd = dict()
for line in handle:
    if line.startswith("From "):
        key = line.split()[1]
        ddd[key] = ddd.get(key, 0) + 1

print ddd
bigCount = None
bigMail = None
for mail, count in ddd.items():

    if bigCount is None or count > bigCount:
        bigCount = count
        bigMail = mail

print bigMail, bigCount
print ddd.keys()
print ddd.values()
print ddd.items()
