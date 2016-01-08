import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://python-data.dr-chuck.net/comments_195272.xml'

print 'Retrieving', serviceurl
uh = urllib.urlopen(serviceurl)
data = uh.read()
print 'Retrieved', len(data), 'characters'
# print data
tree = ET.fromstring(data)

results = tree.findall('comments/comment')
print 'Retrieved', len(results)
sum = 0
for comment in results:
    sum += int(comment.find("count").text)

print sum
