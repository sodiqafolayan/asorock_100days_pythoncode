# collections module in python implements special container data types
# and provide alternative to with some additional functionality
# compared to the general in-built containers like dictionaries,
# lists, tuples. Five different types of collection modules include
# Counter, namedtuple, OrderedDict, defaultdict, deque

# Counter
from collections import Counter
# Counter stores elements as dictionary keys and their count as values

my_string = "aaabbcccccc"  # we can use other iterables too like lists etc
my_counter = Counter(my_string)
print(my_counter)
# Counter({'c': 6, 'a': 3, 'b': 2})
print(my_counter.items())
# dict_items([('a', 3), ('b', 2), ('c', 6)])
print(my_counter.keys())
# dict_keys(['a', 'b', 'c'])
print(my_counter.values())
# dict_values([3, 2, 6])
print(list(my_counter.elements()))
# ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c']
print(my_counter.most_common(1))
# [('c', 6)] # returns a list of tuple of the first most common element
print(my_counter.most_common(2))
# [('c', 6), ('a', 3)] # returns a list of tuple of the second most common element
print(my_counter.most_common(1)[0][0])
# c
print(my_counter.most_common(1)[0][1])
# 6
