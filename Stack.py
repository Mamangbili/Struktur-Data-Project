from Linked_list import Linked,iterate

class Stack:
    def __init__(self):
        self.stack = Linked()
    
    def push(self,val):
        self.stack.add_last(val)

    def pop(self):
        return self.stack.pop()

    def __len__(self):
        return len(self.stack)

    def __repr__(self) -> str:
        return self.stack.__str__()

