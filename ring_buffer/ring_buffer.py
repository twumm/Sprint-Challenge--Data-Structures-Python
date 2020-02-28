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
        if self.storage.length < self.capacity:
            # add item to end of self.storage
            self.storage.add_to_tail(item)
            self.current = self.storage.head
            # set node as current
            # self.current = tail_value
            self.items.append(self.current)
        # if self.size is self.capacity
        elif self.storage.length == self.capacity:
            # remove head and add to tail
            remove_head = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)

            # Reset current position to tail
            if remove_head == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current_node = self.current
        list_buffer_contents.append(current_node.value)
        if current_node.next:
            next_node = current_node.next
        else:
            next_node = self.storage.head # from the top
        # iterate till current node
        while next_node != current_node:
            list_buffer_contents.append(next_node.value)
            if next_node.next: # node to the right? set next_node
                next_node = next_node.next
            else:
                next_node = self.storage.head # go back to head

        return list_buffer_contents
        ######### Almost worked!!
        # while len(self.items) > 0:
        #     current_head = self.storage.remove_from_head()
        #     if current_head is not None:
        #         list_buffer_contents.append(current_head)
        #     self.items.pop(0)
        #     # print(current_head)
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
