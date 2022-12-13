from Linked_list import Linked,iterate
from myQueue import Queue
from vertex import Vertex
from Hash_Table import Hash_Table, iterate_table
from Priority_Queue import Min_Priority_Queue
import tkinter as tk
import random 

vertices = Hash_Table(10)
vertices.add(1,Vertex(1,3))
vertices.add(2,Vertex(4,1))
vertices.add(3,Vertex(5,6))
vertices.add(4,Vertex(2,5))

graph = Hash_Table(10)
graph.add(vertices[1],[vertices[2],vertices[3],vertices[4]])
graph.add(vertices[2],[vertices[1],vertices[3],vertices[4]])
graph.add(vertices[3],[vertices[2],vertices[1],vertices[4]])
graph.add(vertices[4],[vertices[2],vertices[3],vertices[1]])
 

class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('800x600')
        self.window.title('Graph Animation')


        self.window.mainloop()

class generateVertex:
    def __new__(self,n):
        self.vertices = Hash_Table(n)
        for i in range(n):
            x = random.randint(100,600)       # ini ganti lagi nanti sesuai canvas
            y = random.randint(50,550)       # ini ganti lagi nanti sesuai canvas
            self.vertices.add(i, Vertex(x,y) )

        return self.vertices

    def __repr__(self) -> str:
        return str(self.vertices)

class Graph:
    def __init__(self, vertices : Vertex = None):
        self.vertices : Hash_Table = vertices
        self.graph = Hash_Table()
    
    def build_complex_graph(self):
        pass
    
    def add_vertex(self,nama :int | str, vertex : Vertex):
        self.vertices.add(nama, vertex )  

    def add_edge(self,vertex1 : Vertex, vertex2 : Vertex):
        self.graph.add(vertex1, vertex2)    #tambah vertex 2 di key vertex 1
        self.graph.add(vertex2, vertex1)    #tambah vertex 1 di key vertex 2

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

if __name__ == '__main__':
    pass

    