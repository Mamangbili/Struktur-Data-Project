from Linked_list import Linked,iterate
from vertex import Vertex
from Hash_Table import Hash_Table, iterate_table
import random

class generateVertex:
    def __new__(self,n: int, x_max: int, y_max: int):
        self.vertices = Hash_Table(10)
        for i in range(n):
            x = random.randint(50,x_max)       # ini ganti lagi nanti sesuai canvas
            y = random.randint(50,y_max)       # ini ganti lagi nanti sesuai canvas

            if self.__contain(Vertex(x,y)):     
                x,y = x+27,y+27    #agar tidak duplikat tambah dgn angka random
                
            self.vertices.add(i, Vertex(x,y) )
        return self.vertices
    
    def __contain(self, vertex: Vertex):
        try :
            index = hash(vertex)
            self.vertices[index]
            return True
        except:
            return False

    def __repr__(self) -> str:
        return str(self.vertices)
        
class Graph:
    def __init__(self, vertices : Hash_Table = Hash_Table(10)):
        self.vertices : Hash_Table = vertices
        self.graph = Hash_Table(10)
    
    def build_complex_graph(self):
        for i,vertex_key in iterate_table(self.vertices):
            for x,vertex_val in iterate_table(self.vertices):
                if i==x: continue # agar tidak ada self loop
                self.add_edge(vertex_key,vertex_val)
    
    def add_vertex(self,nama :int | str, vertex : Vertex):
        self.vertices.add(nama, vertex )  

    def add_edge(self,vertex1 : Vertex, vertex2 : Vertex):
       #---------------cek apakah vertex ada dalam set atau tidak---------
        vertex1_in_vertices = False 
        vertex2_in_vertices = False
        for i,vertex in iterate_table(self.vertices):
            if vertex1 == vertex : vertex1_in_vertices = True
            if vertex2 == vertex : vertex2_in_vertices = True
 
        if not (vertex1_in_vertices and vertex2_in_vertices):
            raise Exception('Vertex tidak ditemukan dalam set')
        #----------------------------------------------------------------------

        if self.graph == 0:      #graph masih belum ada edge
            self.graph.add(vertex1,vertex2)
            self.graph.add(vertex2,vertex1)      # buat key baru
            return

        #jika key vertex1  sudah ada langsung tambahkan    
        try:
            v1 :list = self.graph.get_val(vertex1)
            if not(vertex2 in v1): #jika sudah tersambung tidak perlu disambung lagi
                v1.append(vertex2)
        except:
        #jika belum ada maka dibuat key baru
            self.graph.add(vertex1, [vertex2])

        #jika key vertex2 sudah ada langsung tambahkan    
        try:
            v2 :list = self.graph.get_val(vertex2)
            if not(vertex1 in v2): #jika sudah tersambung tidak perlu disambung lagi
                v2.append(vertex1) 
        except:
        #jika belum ada maka dibuat key baru
            self.graph.add(vertex2,[vertex1])

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

    def reset(self):
        self.vertices = Hash_Table(10)
        self.graph = Hash_Table(10)