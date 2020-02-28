from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../ring_buffer')
# from doubly_linked_list_one import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.items = []

    def append(self, item):
        # create an empty list to keep track of oldest element
        # if self.size is not self.capacity
        if len(self.items) < self.capacity:
            # add item to end of self.storage
            self.storage.add_to_tail(item)
            tail_value = self.storage.tail
            # set node as current 
            self.current = tail_value
            self.items.append(self.current)
        # if self.size is self.capacity
        else:
            # remove current item
            print(self.current)
            self.storage.delete(self.current)
            self.items.remove(self.current)
            # add item to tail
            self.storage.add_to_tail(item)
            # self.current = self.storage.tail
            # self.items.append(self.current)
            # print(self.items)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        while len(self.items) > 0:
            current_head = self.storage.remove_from_head()
            if current_head is not None:
                list_buffer_contents.append(current_head)
            self.items.pop(0)
            # print(current_head)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

buffer = RingBuffer(5)
buffer.append(3)
buffer.append(2)
buffer.append(4)
buffer.append(1)
buffer.append(4)
buffer.append(7)
buffer.append(9)
print(buffer.get())