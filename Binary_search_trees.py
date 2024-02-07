#defining class of nodes of tree 
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
#difining function to insert value to tree
def tree_insert(node, key):
    if node is None:
        return TreeNode(key)

    if key < node.key:
        node.left = tree_insert(node.left, key)
    elif key > node.key:
        node.right = tree_insert(node.right, key)

    return node

#defining function to tree search
def tree_search(node, key):
    if node is None or key == node.key:
        return node

    if key < node.key:
        return tree_search(node.left, key)
    else:
        return tree_search(node.right, key)

#defining function to eterative tree search
def iterative_tree_search(node, key):
    while node is not None and key != node.key:
        if key < node.key:
            node = node.left
        else:
            node = node.right

    return node

#defining function for tree minimum
def tree_minimum(node):
    while node.left is not None:
        node = node.left
    return node

#defining function for tree maximum
def tree_maximum(node):
    while node.right is not None:
        node = node.right
    return node

#defining function for in order tree walk
def inorder_tree_walk(node):
    if node is not None:
        inorder_tree_walk(node.left)
        print(node.key, end=" ")
        inorder_tree_walk(node.right)

# example use of definitions
keys = [5, 3, 8, 2, 4, 7, 9, 1, 6]
tree_node = None

#inserting keys to tree
for key in keys:
    tree_node = tree_insert(tree_node, key)

#inorder walk of tree. This gives sorted array of keys
print("Inorder tree walk:")
inorder_tree_walk(tree_node), print("\n")

#searching for key 4
searching_key = 4

result = tree_search(tree_node, searching_key)
if result:
    print(f"Key {searching_key} found!")
else:
    print(f"Key {searching_key} not found.")

#finding min and max keys of the tree
min_node = tree_minimum(tree_node)
max_node = tree_maximum(tree_node)

print(f"Minimum key: {min_node.key}")
print(f"Maximum key: {max_node.key}")
