# Lists, tuples, dictionaries, and sets are all iterable objects.
# key must be unique and immutable

dict= {}

dict[0] = "a"
dict[1] = "b"
dict['x'] = 1

print(dict) # {0:'a', 1:'b'}
print(dict.values()) # array of values
print(dict.items()) # [(key, value)] = [(tuple)]

for key, value in dict.items():
    print(key, value)

# print(dict[3]) # dict gives keyError when key is missing but defaultdict handles that

# Syntax: defaultdict(default_factory)
# default_factory: A function returning the default value for the dictionary defined. 
# If this argument is absent then the dictionary raises a KeyError.
from collections import defaultdict
dict1 = defaultdict(list)

dict1[0] = 'A'
dict1[1].append('C')

print(dict1.get(2, 1)) # find key 2's value if not present print default 1



# both create sets
set1= {list}
set2= set()
