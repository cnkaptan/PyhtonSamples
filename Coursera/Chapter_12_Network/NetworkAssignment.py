# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

count = 0
sum = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    count += 1
    sum += int(tag.contents[0])

print "Count", count
print "Sum", sum



# Look at the parts of a tag
# print 'TAG:', tag
# print 'URL:', tag.get('href', None)
# print 'Contents:', tag.contents[0]
# print 'Attrs:', tag.attrs
