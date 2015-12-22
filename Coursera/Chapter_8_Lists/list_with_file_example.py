fHand = open('mbox-short.txt')
for line in fHand:
    line = line.strip()
    if not line.startswith("From "):
        continue
    words = line.split()
    print words
    print words[2]
