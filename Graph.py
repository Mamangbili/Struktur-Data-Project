from Linked_list import Linked,iterate
from vertex import Vertex
from Hash_Table import Hash_Table, iterate_table
import random

class generateVertex:
    def __new__(self,n : int):
        self.vertices = Hash_Table(10)
        for i in range(n):
            x = random.randint(100,600)       # ini ganti lagi nanti sesuai canvas
            y = random.randint(50,550)       # ini ganti lagi nanti sesuai canvas
            self.vertices.add(i, Vertex(x,y) )

        return self.vertices

    def __repr__(self) -> str:
        return str(self.vertices)
        
class Graph:
    def __init__(self, vertices : Hash_Table = None):
        self.vertices : Hash_Table = vertices
        self.graph = Hash_Table(10)
    
    def build_complex_graph(self):
        pass
    
    def add_vertex(self,nama :int | str, vertex : Vertex):
        self.vertices.add(nama, vertex )  

    def add_edge(self,vertex1 : Vertex, vertex2 : Vertex):
        try:
            v1 = self.vertices.get_val(vertex1)
            v2 = self.vertices.get_val(vertex2)             #dicek apakah vertex ada dalam self.vertices
        except:
            raise Exception("Vertex argument tidak ada dalam himpunan vertex")
        
        if self.graph == 0:      #graph masih belum ada edge
            self.graph.add(vertex1,vertex2)
            self.graph.add(vertex2,vertex1)      # buat key baru
            return

        #jika key vertex1  sudah ada langsung tambahkan    
        try:
            v1 :list = self.graph.get_val(vertex1)
            v1.append(vertex2)
        except:
        #jika belum ada maka dibuat key baru
            self.graph.add(vertex1, vertex2)

        #jika key vertex2 sudah ada langsung tambahkan    
        try:
            v2 :list = self.graph.get_val(vertex2)
            v2.append(vertex1) 
        except:
        #jika belum ada maka dibuat key baru
            self.graph.add(vertex2,vertex1)

    def delete_vertex(self,vertex : Vertex):
        self.graph.delete_key(vertex)
        found = False
        for key,val in iterate_table(self.vertices):  #iterate ke semua node $Vertices untuk mencari dan menghapus vertex
            if  val == vertex:
                found = True
                self.vertices.delete_key(key)  

        if found == False: raise Exception('Vertex tidak ditemukan')

        for key,val in iterate_table(self.graph): #hapus key vertex yg dicari
            if key == vertex:
                self.graph.delete_key(vertex)
            
            if vertex in val:               #kemudian hapus edge yg berhubungan dengan vertex lama yg telah dihapus
                val.remove(vertex)
        
    def delete_edge(self,vertex1 : Vertex, vertex2 : Vertex):
        try:
            self.graph[vertex1].remove(vertex2)         # hapus vertex 2 dari himpunan edge vertex 1
            self.graph[vertex2].remove(vertex1)         # hapus vertex 1 dari himpunan edge vertex 2
        except:
            raise Exception(f'Tidak ada edge {vertex1}-{vertex2}')
