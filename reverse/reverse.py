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

    def reverse_list(self, node, prev):
        if node is None:
            return
        node = self.head
        prev = None
        #check if the current node is the tail
        while node is not None:
            current_value = node.get_next()
            node.set_next(prev)
            prev = node
            node = current_value
        self.head = prev
        # if current_node == node:
        #     return
        # current_node.next_node = self.head
        # self.head = current_node
        # self.reverse_list(self.head, None)

list = LinkedList()

list.add_to_head(1)
list.add_to_head(2)
list.add_to_head(3)

print(list.head.value)

list.reverse_list(list.head, None)

print(list.head.value)

            
        

        
