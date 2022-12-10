from Linked_list import Linked,iterate
from myQueue import Queue
from vertex import Vertex
from Hash_Table import Hash_Table, iterate_table
from Priority_Queue import Min_Priority_Queue

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
 
for x,i in iterate_table(graph):
    print('key ',x,'val ',i)