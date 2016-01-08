import urllib
from BeautifulSoup import *

html = urllib.urlopen("https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Iqra.html").read()
soup = BeautifulSoup(html)

count = int(raw_input("Enter Count:"))
position = int(raw_input("Enter Position:"))

# Retrieve all of the anchor tags
tags = soup('a')

for k in range(count):
    counter = 1
    for tag in tags:
        if (counter == position):
            print tag.contents[0]
            soup = BeautifulSoup(urllib.urlopen(tag.get('href', None)).read())
            tags = soup('a')
            break
        counter += 1
