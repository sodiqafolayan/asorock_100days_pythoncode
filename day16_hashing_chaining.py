# https://practice.geeksforgeeks.org/tracks/DS-Python-Hashing/?batchId=273

class MyHashTable:
    def __init__(self, b): # this defines the instance variable and will be different (except we provide 
                                # same variable) for each instance/object
        # BUCKET is used here just to be verbose. The convention is to write self.b = b
        # Since self.BUCKET = b, self.BUCKET now holds the max size of our would-be table
        # ie if b is 10, our bucket size (hash rows) will be 0-9
        self.BUCKET = b
        self.table = [[] for x in range(b)]
        # We created a table (ie list of lists) above with the outer most [ ] and created inner lists 
        # equal to the size of our bucket

    # Class method/function
    def insert(self, x):
        i = x % self.BUCKET
        self.table[i].append(x)

    # Class method/function
    def remove(self, x):
        i = x % self.BUCKET
        if x in self.table[i]:
                self.table[i].remove(x)
        
    # Class method/function
    def search(self, x):
        i = x % self.BUCKET
        return x in self.table[i]

aso = MyHashTable(3)
print("Insert 56 below")
aso.insert(56)
print("Insert 27 below")
aso.insert(27)
print("Insert 12 below")
aso.insert(12)
print("Remove 27 below")
aso.remove(27)
print("Remove 100 below")
aso.remove(100)
print("Search 20 below")
aso.search(20)

print(aso.table)
print(aso.BUCKET)