class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev=None):
        #check to see if list is empty
        if node is None:
            return
        #set current_node as self.head
        current_node = node
        #set previous value at None to start (default value)
        #iterate through new list until current_node is none
        while current_node is not None:
            #create placeholder for next node to look ate
            place_holder = current_node.get_next()
            #Add node to beginning of new list by making it point to previous node (first node will point to None)
            current_node.set_next(prev)
            #Reset previous node to current_node
            prev = current_node
            #Reset current_node to place_holder
            current_node = place_holder
        self.head = prev
    
linked_list = LinkedList()
linked_list.add_to_head(1)
linked_list.add_to_head(2)
linked_list.add_to_head(3)


print(linked_list.head.value)

linked_list.reverse_list(linked_list.head)

print(linked_list.head.value)