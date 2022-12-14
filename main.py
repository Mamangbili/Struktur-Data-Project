from Graph import Graph, generateVertex
import tkinter as tk
from vertex import Vertex
t = generateVertex(5)
g = Graph(t)


print(g.vertices)

# g.add_edge(g.vertices[1],g.vertices[2])
g.add_edge(g.vertices[1],g.vertices[0])
g.add_edge(g.vertices[1],g.vertices[2])
# g.add_edge(g.vertices[2],g.vertices[3])

print(g.graph)
# g.reset()

