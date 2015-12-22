import re

str = 'an example word:cat!!'
# bastaki r burda rawi temsil eder
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:
    print 'found', match.group()  ## 'found word:cat'
else:
    print 'did not find'

print "\n"

# a, X, 9, < -- ordinary characters just match themselves exactly. The meta-characters which do not match themselves
# because they have special meanings are: . ^ $ * + ? { [ ] \ | ( ) (details below)
#
# . (a period) -- matches any single character except newline '\n'
#
# \w -- (lowercase w) matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_]. Note that although "word"
# is the mnemonic for this, it only matches a single word char, not a whole word. \W (upper case W) matches any
# non-word character.
#
# \b -- boundary between word and non-word
#
# \s -- (lowercase s) matches a single whitespace character -- space, newline, return, tab, form [ \n\r\t\f]. \S (upper
# case S) matches any non-whitespace character.
#
# \t, \n, \r -- tab, newline, return
#
# \d -- decimal digit [0-9] (some older regex utilities do not support but \d, but they all support \w and \s)
#
# ^ = start, $ = end -- match the start or end of the string
#
# \ -- inhibit the "specialness" of a character. So, for example, use \. to match a period or \\ to match a slash.
#  If you are unsure if a character has special meaning, such as '@', you can put a slash in front of it, \@, to make
#  sure it is treated just as a character.


# Search for pattern 'iii' in string 'piiig'.
# All of the pattern must match, but it may appear anywhere.
# On success, match.group() is matched text.

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)
if match:
    print match.group()  ## 'b@google'
print "\n"
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search('([\w.-]+)@([\w.-]+)', str)
if match:
    print match.group()  ## 'alice-b@google.com' (the whole match)
    print match.group(1)  ## 'alice-b' (the username, group 1)
    print match.group(2)  ## 'google.com' (the host, group 2)

print "\n"
# Suppose we have a text with many email addresses
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

# Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str)  # ['alice@google.com', 'bob@abc.com']
for email in emails:
    # do something with each found email string
    print email

print "\n"

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print tuples  # [('alice', 'google.com'), ('bob', 'abc.com')]
for tuple in tuples:
    print tuple[0]  # username
    print tuple[1]  # host

print "\n"
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
# re.sub(pat, replacement, str) -- returns new string with all replacements,
# \1 is group(1), \2 group(2) in the replacement
print re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str)
# purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher


str = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
r = re.search(r'\S+?@\S+', str)
print r.group()
