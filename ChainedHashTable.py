# defining class for chained hash
class ChainedHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    #Defining function of hash insert
    def hash_insert(self, key, value):
        memory_index = self.hash_function(key)
        if self.table[memory_index] is None:
            self.table[memory_index] = []
        self.list_prepend(self.table[memory_index], (key, value))

    #Defining function of hash search
    def hash_search(self, key):
        memory_index = self.hash_function(key)
        if self.table[memory_index] is not None:
            return self.list_search(self.table[memory_index], key)
        return None

    #Defining function of hash delete
    def hash_delete(self, key):
        memory_index = self.hash_function(key)
        if self.table[memory_index] is not None:
            self.list_delete(self.table[memory_index], key)
    
    #defining hash function
    def hash_function(self,key):
        memory_index = key % self.size
        return memory_index

    #defining function for prepending
    @staticmethod
    def list_prepend(List_of_elements, element):
        List_of_elements.insert(0, element)

    #defining function for searching
    @staticmethod
    def list_search(List_of_elements, key):
        for k, v in List_of_elements:
            if k == key:
                return v
        return None

    #defining function for deleting
    @staticmethod
    def list_delete(List_of_elements, key):
        for i, (k, _) in enumerate(List_of_elements):
            if k == key:
                del List_of_elements[i]
                break

# example use of the above class
table = ChainedHashTable(8)  # creating a table of size 8
table.hash_insert(7, "Value_1")  # inserting values into the table
table.hash_insert(8, "Value_2")  # inserting values into the table
print(table.hash_search(7))  # output should be "Value_1"
table.hash_delete(7)
print(table.hash_search(7))  # output should be "None"