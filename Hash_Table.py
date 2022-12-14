from Linked_list import *

class Hash_Table:
    def __init__(self,length):
        self.table = [None]*length
        self.length = length

    def __len__(self):
        return self.length - self.table.count(None)

    def __get_index(self,key):
        index = hash(key) % self.length
        return index

    def __find_key(self,key):
        index = self.__get_index(key)
        if self.table[index] is None:
            raise KeyError('Key not found')

        #cari key di kolom index tersebut
                                         #LINKED list 
        kolom = self.table[index]
        for i,node in enumerate(iterate(kolom),0):
            if node.key == key :
                return i

        #raise error jika key tidak ditemukan
        raise KeyError('Key not found')

    def get_val(self,key):
        index = self.__get_index(key)
        i_kolom = self.__find_key(key)
                #cari row           #cari kolom
        return self.table[index].findVal(i_kolom)  #return list vertices 

    def change_val(self,key,data):
        index = self.__get_index(key)
        i_kolom = self.__find_key(key)
        
        kolom_value = self.table[index].findVal(i_kolom)
        self.table[index].change_value(kolom_value, data)
        return self
        
    def add(self,key,val =0):
        index = self.__get_index(key)
        row = self.table[index]
        if row is None:
            self.table[index] = Linked()
            self.table[index].add_last(val,key)
        else : 
            self.table[index].add_last(val,key)
        return self

    def delete_key(self,key):
        index = self.__get_index(key)
        if self.table[index] is None:
            raise KeyError('Key not found')

        row = self.table[index]
        for item,i in iterate(row):
            if item.key == key:
                item.pop(i)
                return self
        raise KeyError('Key not found')

    def __repr__(self) -> str:
        return self.__str__()
    
    def __str__(self) -> str:
        table_repr ={}
        for row in self.table:
            if row is None:
                continue
            else:
                for kolom_key in iterate(row): #linked list
                    table_repr[kolom_key.key] = kolom_key.data

        return str(table_repr)

    def __iter__(self):
        for x in self.table:
            yield x

    def __getitem__(self,key):
        return self.get_val(key)
        

 
def iterate_table(table):
    for row in iterate(table):
        if row is not None:
            for node in iterate(row):
                yield (node.key,node.data)


