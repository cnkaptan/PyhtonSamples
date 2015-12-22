name = raw_input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

ddd = dict()
for line in handle:
    if line.startswith("From "):
        key = line.split()[5].split(":")[0]
        ddd[key] = ddd.get(key, 0) + 1

for p, r in sorted(ddd.items()):
    print p, r
