from Linked_list import *

class Queue:
    
    def __init__(self):
        self.stack = Linked()
    
    def __iter__(self):
        return self

    def __next__(self):
        return self.stack.__next__()

    def queue(self,val):
        self.stack.add_last(val)
        return self

    def dequeue(self):
        return self.stack.pop(0)      

    def top(self):
        return self.stack.findVal()

# a = Queue()
# a.queue(1)
# a.queue(2)
# a.queue(3)

# m = Linked()
# m.add_last(1)
# m.add_last(2)
# m.add_last(3)

# for x in iterate(m):
#     print(x)
#     if x == 2:
#         break
# for x in iterate(m):
#     print('baru')


