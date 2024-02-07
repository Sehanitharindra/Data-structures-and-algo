#dreating class for hash table
class DirectAddressTable:
    def __init__(self, size):
        self.table = [None] * size

    #defining insert function
    def insert(self, key, value):
        self.table[key] = value

    #defining delete function
    def delete(self, key):
        self.table[key] = None

    #defining search function
    def search(self, key):
        return self.table[key]

# example use of functions
#creating table of size 10
table = DirectAddressTable(10)
#insert values to table
table.insert(3, "Value_1")
table.insert(5, "Value_2")
# searching for value 3
print(table.search(5))  # output should be value_2
# deleting value 3
table.delete(3)
print(table.search(3))  # output should be None
