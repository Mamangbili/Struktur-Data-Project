from Graph import Graph, generateVertex
import tkinter as tk
from vertex import Vertex

t = generateVertex(5)
g = Graph(t)

print(g.vertices,'\n')
g.build_complex_graph()
print(g.graph)