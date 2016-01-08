import json
import urllib
serviceurl = 'http://python-data.dr-chuck.net/comments_195276.json'

print 'Retrieving', serviceurl
uh = urllib.urlopen(serviceurl)
data = uh.read()
print 'Retrieved', len(data), 'characters'
# print data

info = json.loads(data)
# print 'User count:', len(info["comments"])
sum = 0

for comment in info["comments"]:
    sum += int(comment['count'])

print sum

