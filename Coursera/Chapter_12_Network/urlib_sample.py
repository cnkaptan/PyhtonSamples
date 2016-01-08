import urllib
from BeautifulSoup import *

fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

# for line in fhand:
#     print line.strip()

print "\n"

# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
#
# print counts

print "\n"

# fhand = urllib.urlopen("http://www.dr-chuck.com/page1.htm")
#
# for line in fhand:
#     print line.strip()


# url = raw_input("Enter - ")
#
# html = urllib.urlopen(url).read()
# soup = BeautifulSoup(html)
#
# tags = soup('a')
#
# for tag in tags:
#     print tag.get("href", None)
