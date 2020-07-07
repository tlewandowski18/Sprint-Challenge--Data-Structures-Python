class RingBuffer:
    def __init__(self, capacity):
        #set capacity of list at passed in value
        self.capacity = capacity
        #create storage for list in form of array
        self.storage = []
        #create index variable that will represent the oldest item in the array
        self.oldest_index = 0

    def append(self, item):
        #check to see if list is at capacity
        if len(self.storage) < self.capacity:
            #if not at capacity, add item to end of list
            self.storage.append(item)
        else:
            #if at capacity replace item at oldest_index with new item
            self.storage[self.oldest_index] = item
            #check to see if oldest_index is at the end of the list
            if self.oldest_index < self.capacity - 1:
                #if oldest_index is not at the end of the list, increase that index by one
                self.oldest_index += 1
            else:
                #if oldest_index is at end of list, return it to beginning of list
                self.oldest_index = 0

    def get(self):
        #create a new list
        new_list= []
        #iterate through storage and add any items to list that aren't "None"
        for i in self.storage:
            if i is not None:
                new_list.append(i)
        #return new list
        return new_list

ring_buffer = RingBuffer(5)

ring_buffer.append('a')
ring_buffer.append('b')
ring_buffer.append('c')
ring_buffer.append('d')
ring_buffer.append('e')

print(ring_buffer.get())

ring_buffer.append('f')
ring_buffer.append('g')
ring_buffer.append('h')

print(ring_buffer.get())