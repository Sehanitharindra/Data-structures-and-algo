#defining class for linear probing hash table
class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

#defining function to insert
    def insert(self, key ):
        memory_index = self.hash_function(key)
        initial_memory_index = memory_index
        while True:
            if self.table[memory_index] is None:
                self.table[memory_index] = (key) # inserting the key in right place
                break
            else:
                memory_index = (memory_index + 1) % self.size
            if memory_index == initial_memory_index:
                print("Overflow") # this is to avoid ifinite loop
                break
        
    #defining function for searching 
    def search(self, key):
        memory_index = self.hash_function(key)
        initial_memory_index = memory_index
        while self.table[memory_index] is not None:
            k = self.table[memory_index]# returning memory_index, if key is in the table
            if k == key:
                return memory_index
            else:
                memory_index = (memory_index + 1) % self.size
            if memory_index == initial_memory_index:
                break  # this is to avoid ifinite loop

#defining function for deleting
    def delete(self, key):
        memory_index = self.hash_function(key)
        initial_memory_index = memory_index
        while self.table[memory_index] is not None:
            k = self.table[memory_index]
            if k == key: # making memory_index memory place as None, if the key is in the table
                self.table[memory_index] = None
                return 
            else:
                memory_index = (memory_index + 1) % self.size
            if memory_index == initial_memory_index:
                break  # this is to avoid ifinite loop
    

    def hash_function(self,key):
        memory_index = (key) % self.size
        return memory_index

# example use of functions
table_size = 10
table = LinearProbingHashTable(table_size)

#inserting keys to table
keys = [11, 25, 37, 50, 28, 46, 9, 18]
for key in keys:
    table.insert(key)

#printing keys and its memory_indexes to make sure implementation is correct
for key in keys:
    print(key, table.search(key)) # here we can see in the output that 28 is in 8 and 18 is in 2. that means it works correctly

table.insert(3)
print(table.search(3))  # output is 3
table.delete(3)
print(table.search(3))  # output comes as None
