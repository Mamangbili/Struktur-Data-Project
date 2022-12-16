from Linked_list import Linked,iterate

class Stack:
    def __init__(self):
        self.stack = Linked()
    
    def push(self,val):
        self.stack.add_last(val)

    def __iter__(self):
        return self

    def __next__(self):
        return self.stack.__next__()

    def pop(self):
        self.stack
        return self.stack.pop()

    def __len__(self):
        return len(self.stack)

    def __repr__(self) -> str:
        return self.stack.__str__()

a = Stack()
a.push(2)
a.push(3)
a.push(4)

for x in range(len(a)):
    print(a.pop())
