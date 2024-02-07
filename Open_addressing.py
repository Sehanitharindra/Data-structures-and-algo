# Defining class of hash table
class Hashtable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

# defining function of inserting
    def hash_insert(self, key):
        i = 0
        while i < self.size:
            q = self.hash_function(key, i)
            if self.table[q] is None:
                self.table[q] = key
                return q
            else:
                i += 1
                return i
        raise OverflowError("hash table overflow")

# defining function of searching
    def hash_search(self, key):
        i = 0
        while True:
            q = self.hash_function(key, i)
            if self.table[q] == key:
                return q
            i += 1
            if self.table[q] is None or i == self.size:
                return None

# defining function of deleting
    def hash_delete(self, key):
        i = 0
        q = self.hash_function(key, i)
        if self.table[q] == key:
            self.table[q] = None
            return key # since when q is set to None, there is no value in q.
        i += 1
        if self.table[q] is None or i == self.size:
            return None   
                  
# defining hash function
    def hash_function(self, key, i):
        return (key + i) % self.size


# example use of functions
table_size = 9
table = Hashtable(table_size)

#inserting keys to table
keys = [11, 25, 37, 50, 28, 46, 9]
for key in keys:
    table.hash_insert(key)

#searching a key
key = 25
result = table.hash_search(key)
if result is not None:
    print(f"Key {key} found at index {result}")
else:
    print(f"Key {key} not found")

#searching a key
key = 9
result = table.hash_search(key)
if result is not None:
    print(f"Key {key} found at index {result}")
else:
    print(f"Key {key} not found") 

#deleting key
key = 25
table.hash_delete(key)
result = table.hash_search(key)
if result is not None:
    print(f"Key {key} found at index {result}")
else:
    print(f"Key {key} not found")