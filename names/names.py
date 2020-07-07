class BSTNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #compare new value to current value of node
        #passed value is less than or equal to node's value
        if self.value is None:
            self.value = value
        elif value < self.value:
            #if there is no left child for Node, insert the value as the left child
            if self.left is None:
                self.left = BSTNode(value)
            #if there is a left child for Node, call the insert function on that Node
            else:
                self.left.insert(value)
        #passed value is greater than the node's value    
        else:
            #if there is no right child for Node, insert the value as the right child
            if self.right is None:
                self.right = BSTNode(value)
            #if there is a right child for Node, call insert on that Node
            else:
                self.right.insert(value)
        
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #check if target is equal to current_value
        if self.value == target:
            return True
        #if target is less than current_value
        elif target < self.value:
            #return false if there is no value less than current value in the tree
            if self.left is None:
                return False
            #if there is a value less than current value, run "contains" on the node containing that value
            return self.left.contains(target)
        #if target is greater than current_value
        else:
            #return false if there is no value greater than current value in the tree
            if self.right is None:
                return False
            #if there is a value less than current value, run "contains" on the node containing that value
            return self.right.contains(target)
        
import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
