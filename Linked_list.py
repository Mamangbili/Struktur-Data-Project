class Node :
    def __init__(self, val = None, key =None):
        self.data = val
        self.next = None
        self.key = key

    def __str__(self) -> str:
        return (f'{str(self.key)} , {str(self.data)}' )
        
        
class Linked :
    def __init__(self):
        self.head = None
        self.length = 0

    def __iter__(self):
        return self

    def __len__(self):
        return self.length

    def __next__(self):
        if self.length == 0:
            raise StopIteration
        current_node = self.head
        self.head = self.head.next
        self.length -= 1
        return current_node
    
    def add_last(self, val,key=None):
        new_node = Node(val,key)
        if self.head == None:
            self.head= new_node
        else :
            current_node = self.head
            while current_node.next:
                current_node = current_node.next 
            current_node.next = new_node
        self.length += 1

    def add_first(self, val,key=None):
        new_node = Node(val,key)
        self.length += 1
        new_node.next = self.head
        self.head = new_node
        
    def insert(self, index, val,key=None):
        assert 0<=index<self.length, "Index out of range"
        if index == 0:
            self.add_first(val,key)
            return
        new_node = Node(val,key)
        current_node = self.head
        for x in range(index-1):
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node
        self.length += 1
        
    def pop(self,index=None):
        '''index empty == pop last item'''
        if index is None:
            index = self.length-1 #hapus index akhir jika argumen kosong
        assert (0<= index < self.length) , "Index out of range"
        
        if index == 0:
            data = self.head.data
            self.head = self.head.next
            self.length -=1
            return data
        
        current_node = self.head
        
        for x in range(index-1):
            current_node = current_node.next 
        deleted_node = current_node.next
        data = deleted_node.data
        current_node.next = deleted_node.next
        self.length -=1 
        return data
        
    def findVal(self, index):
        '''find item by indexing, start from index 0'''
        current_node = self.head
        while index > 0:
            current_node = current_node.next
            index-=1
        return current_node.data
    
    def __repr__(self):
        current_node = self.head
        listSet = "["
        while current_node.next:
                listSet +=  str(current_node.data) + ',' 
                current_node = current_node.next
    
        listSet +=  str(current_node.data) + ']'
        return listSet
    
    def getLength(self):
        return self.length

    def union(self, linkedList):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = linkedList.head  

    def Sum (self):
        current_node = self.head
        Sum = 0
        while current_node.next:
            Sum += current_node.data
            current_node = current_node.next
        Sum += current_node.data
        return Sum

    def autoSortAdd (self, val,key=None):
        new_node = Node(val,key)
        current_node = self.head

        if self.head is None:
            self.head = new_node
            self.length += 1
            return

        while current_node.next and val > (current_node.next).data :
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node
        self.length += 1

    def reverseList(self):
        current_node = self.head
        prev_node = None

        if self.head == None or self.head.next == None:
            return

        while current_node.next:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            
        self.head = next_node
        next_node.next = prev_node

    def sort_linked_list(self):
        current = self.head  
        next_node = self.head.next
        prev_node = current
        if(self.head == None) or (self.head.next is None):  
            return  
        else:  
            while prev_node.next:
                while next_node.next:
                    if current.data > next_node.data:
                        current.data, next_node.data = next_node.data, current.data

                    next_node = next_node.next
                    current = current.next
                else : 
                    next_node = next_node.next
                    current = current.next
                    if current.data > next_node.data:
                        current.data, next_node.data = next_node.data, current.data
                
                prev_node = prev_node.next

    def change_value(self,index,val):
        current_node = self.head
        if not -self.length<=index<self.length:
            raise IndexError('List index out of range')

        if index < 0:
            index = self.length + index

        while index > 0:
            current_node = current_node.next
            index-=1
        current_node.data = val
        
        return self

def iterate(iterable):
    from copy import copy
    for x in copy(iterable):
        yield x

# a = Linked()
# a.add_last(2)
# a.add_last(3)
# a.add_last(4)

# for x in iterate(a):
#     print(x.data)














