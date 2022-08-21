# Lists, tuples, dictionaries, and sets are all iterable objects.
# key must be unique and immutable

dict= {}

dict[0] = "a"
dict[1] = "b"
dict[2] = "c"
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
dict1 = defaultdict(list) # key = any | value = List (default type)
dict2 = defaultdict(set)  # key = any | value = set (default type)
dict4 = defaultdict(set)  # key = any | value = set (default type)
dict3 = defaultdict(int)  # key = any | value = int (default type)
    
#only List methonds are available
dict1[0] = 'A'
dict1[1].append('C')
dict1[1].append('C')

print(dict1)
print(dict1.get(2, 1)) # find key 2's value if not present print default 1

# only set methods are available
dict2[0].add(1)
dict2[0].add(1)
dict2[0].add(1)
dict2[1].add(2)
dict2[1].add(2)


print(f"Dict-2: {dict2[2]}") # value = set() so no duplicate value entry

# only int methods are available
dict3[0] = 1
dict3[1] = 2
dict3[2] = 3

print(f'Dict-3 {dict3}')
print(dict3[3]) # as no key/value prints '0' as its value type is int

#key = tupple
# dict4[(0,1)].add(1)
# dict4[(0,1)].add(1)
# dict4[(0,2)].add(2)

print(dict4)
print(dict4[(0,2)])
print(dict4[0]) #no this way when key is tuple

#tuple
t = [(0,1), (0,2), (0,3)] # list of tuples

print((t[0]))



# both create sets
set1= {list}
set2= set()
