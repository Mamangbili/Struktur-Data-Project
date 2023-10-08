class Min_Priority_Queue:
    
    def __init__(self):
        self.heap_item = []
        self.size = len(self.heap_item)
    
    def get_left_childIdx (self,parentIdx): return 2*parentIdx + 1       
    def get_right_childIdx (self,parentIdx): return 2*parentIdx + 2
    def get_parentIdx(self, childIdx):
        from math import ceil        
        return  ceil((childIdx - 2) / 2 )    
    
    def has_left(self, parentIdx):
        if self.get_left_childIdx(parentIdx) < self.size:
            return True
        return False
        
    def has_right(self, parentIdx):
        if self.get_right_childIdx(parentIdx) < self.size:
            return True
        return False

    def has_parent(self, childIdx):
        if self.get_parentIdx(childIdx) >= 0 :
            return True
        return False

    def get_left_child (self, parentIdx):     
        if self.has_left(parentIdx):
            return self.heap_item[self.get_left_childIdx(parentIdx)]
        return None
    def get_right_child (self, parentIdx):     
        if self.has_right(parentIdx):
            return self.heap_item[self.get_right_childIdx(parentIdx)]
        return None
    def get_parent(self, childIdx):
        if self.has_parent(childIdx):
            return self.heap_item[self.get_parentIdx(childIdx)]
        return None

    def swap(self,idx1,idx2):
        self.heap_item[idx1] , self.heap_item[idx2] = self.heap_item[idx2], self.heap_item[idx1]
    
    def HeapifyUp(self,idx):
        current_node = self.heap_item[idx]
        parent_node = self.get_parent(idx)
        if parent_node is None :
            return
        if current_node < parent_node:
            parent_idx = self.get_parentIdx(idx)
            self.swap(idx, parent_idx)
            self.HeapifyUp(parent_idx)

    def Heapify_down(self, idx = 0):
        largest = idx
        left_idx = self.get_left_childIdx(idx)
        right_idx = self.get_right_childIdx(idx)

        #cek apakah ada child kiri lalu cek apakah nilainya child kiri > parent
        if left_idx < self.size:
            if self.heap_item[largest] > self.heap_item[left_idx] :
                largest = left_idx
        
        #cek apakah ada child kanan lalu cek apakah nilainya child kiri > child kanan
        if right_idx < self.size:
            if self.heap_item[largest] > self.heap_item[right_idx] :
                largest = right_idx

        #jika terdekesi pertukaran pointer 
        if largest != idx :
            self.swap(idx, largest)
            self.Heapify_down(largest)
        
    def enqueue (self, val):
        self.heap_item.append(val)
        self.HeapifyUp(self.size) #index terakhir
        self.size += 1 #tambah total isi list
        print(self.heap_item)

    def peek(self):
        print(self.heap_item)

    def dequeue(self):
        item = self.heap_item[0]
        self.heap_item[0] = self.heap_item[self.size-1] #copy index terakhir ke index awal 
        self.heap_item.pop()                # hapus index terakhir
        self.size -= 1
        self.Heapify_down()                 #heapify down
        return item                         #hasil dequeu
    
    def dequeue_to (self, target_val):
        while self.heap_item[0] != target_val:
            print(self.dequeue())
        else :
            print(self.dequeue())
