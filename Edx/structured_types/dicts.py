my_dict = {}
grades = {'Ana': 'B', 'John': 'B+', 'Denise': 'A+', 'Katy': 'A'}
print(grades['John'])

# add entry
grades['Cihan'] = "A++"

print(grades)

# key test
print('Cihan' in grades)
print("Cuneyt" in grades)

# delete entry
del (grades['Cihan'])
print(grades)

print('------------------------------------------------------------')

# get an iterable that acts like a tuple of all keys , sirayla olmayabilir

print(grades.keys())

# get an iterable that acts like a tuple of all values , sirayla olmayabilir

print(grades.values())

"""
    values;
        - any type (immutable and mutable)
        - can be duplicates
        - dictionary values can be lists, even other dictionaries
    keys;
        - must be unique
        - immutable type (int,float,string,tuple,bool)
            - actually need an object that is hashable, but think of as immutable as all immutable types are hashable
        - careful with float type as a key
    - no order to key or values!

"""

print('------------------------------------------------------------')

animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati', 'd': 'donkey'}

print(animals)
print(animals['c'])
print(len(animals))

animals['a'] = 'anteater'
print(animals['a'])
print(len(animals['a']))

print('baboon' in animals)
print('donkey' in animals.values())
print('b' in animals)

print(animals.keys())

print(animals)
del animals['b']
print(animals)
print(animals.values())

print('------------------------------------------------------------')

animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey']}

animals['d'].append('dog')
animals['d'].append('dingo')

print(animals)

sum = 0
for key in animals.keys():
    sum += len(animals[key])

print(sum)

biggestLen = 0
biggestKey = ''
for key in animals.keys():
    if biggestLen < len(animals[key]):
        biggestLen = len(animals[key])
        biggestKey = key

print(biggestKey)



