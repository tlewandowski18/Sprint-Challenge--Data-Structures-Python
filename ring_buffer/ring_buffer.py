

class RingBuffer:
    def __init__(self, capacity):
        #set capacity at passed value for capacity
        self.capacity = capacity
        #store items in list
        self.storage = []
        #first oldest item will be the first item on list
        self.oldest_index = 0

    def append(self, item):
        #check to see if Buffer is at capacity
        if len(self.storage) < self.capacity:
            #if not at capacity add newest item to tail of list
            self.storage.append(item)
            #increase size by one
        else:
            #if list is at capacity replace the item at "oldest" index with new item
            self.storage[self.oldest_index] = item
            #update "oldest" index
            #if previous "oldest" index is not last item on list, increase "oldest" index by one
            if self.oldest_index < self.capacity - 1:
                self.oldest_index += 1
            #if previous oldest index is last item on list, return "oldest" index to front item
            else:
                self.oldest_index = 0

    def get(self):
        new_list = []
        #iterate through stored list
        for item in self.storage:
            #add any items to stored list that aren't None
            if item:
                new_list.append(item)
        return new_list


buffer = RingBuffer(5)

buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get())

buffer.append('d')

print(buffer.get())

buffer.append('e')
buffer.append(None)
print(buffer.get())

for i in range(50):
    buffer.append(i)

print(buffer.get())