#defining class for tree node. a tree node has properties, key, left, right, parent and color.
class TreeNode:
    def __init__(self, key, color, left=None, right=None, parent=None):
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

#defining class for red black tree.
class RedBlackTree:
    def __init__(self):
        self.nil = TreeNode(None, "BLACK") # starting making all nodes nil and black
        self.root = self.nil

# function for searching elements.
    def tree_search(self, x, key):
        if x == self.nil or key == x.key:
            return x
        if key < x.key:
            return self.tree_search(x.left, key)
        else:
            return self.tree_search(x.right, key)
        
# this is the function for left rotation. The implementation exact;ly similar to algorithm in book
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

# this is the function for right rotation. The implementation exact;ly similar to algorithm in book
    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.nil:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == self.nil:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x

# function for  inserting keys to tree
    def rb_insert(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = "RED"
        self.rb_insert_fixup(z)

#defining the function for red black tree fix up. when node is inserted we violating red black tre properties and so we have fix up the table
#function has the exact notations in algorithm in the book
    def rb_insert_fixup(self, z):
        while z.parent.color == "RED":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.left_rotate(z.parent.parent)
        self.root.color = "BLACK"

#function for transplant
    def rb_transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

#function for finding tree minimum
    def tree_minimum(self, x):
        while x.left != self.nil:
            x = x.left
        return x

#function for deleting nodes from tree
    #here by deleting elements we violate the properties of tree. So we have to fix up the tree properties
    def rb_delete(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == "BLACK":
            self.rb_delete_fixup(x)

#the function for fixup when an element is deleted.
#we have to maintain the properties of tree
#this contains exact notations of algorithm in book
    def rb_delete_fixup(self, x):
        while x != self.root and x.color == "BLACK":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.right.color == "BLACK":
                        w.left.color = "BLACK"
                        w.color = "RED"
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.right.color = "BLACK"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == "BLACK" and w.left.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.left.color == "BLACK":
                        w.right.color = "BLACK"
                        w.color = "RED"
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.left.color = "BLACK"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "BLACK"

#this function is to print the tree
def tree_printing(node, space=0, start_point="Root: "):
    if node != nil:
        print(" " * (space * 4) + start_point + str(node.key) + " (" + node.color + ")")#printing node with space given by space, key and its colour
        if node.left or node.right:
            tree_printing(node.left, space + 1, "L- ")#recurssive actio for left side
            tree_printing(node.right, space + 1, "R- ")#recurssive action for right side

#initializing nil node
nil = TreeNode(None, "BLACK")

# inserting elements to tree
rb_tree = RedBlackTree()
keys = [41, 38, 31, 12, 19, 8]
for key in keys:
    rb_tree.rb_insert(TreeNode(key, "RED"))

print("tree after inserting elements:")
tree_printing(rb_tree.root)

# deleting
deleting_key = 38
rb_tree.rb_delete(rb_tree.tree_search(rb_tree.root, deleting_key))  # deleting 38
print("\ntree after deleting element:")
tree_printing(rb_tree.root)

#from display of the tree, we can identify the cerrectness of the code.
#this works correctly