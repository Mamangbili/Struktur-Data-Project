from Graph import Graph, generateVertex
import tkinter as tk
from vertex import Vertex
from Hash_Table import Hash_Table,iterate_table
import time

class MyApp:
    def __init__(self):
        #window dan canvas------------------------------------------------------------
        self.root = tk.Tk()
        self.window()
        self.canvas = tk.Canvas(width=800, height=500,background='#b8b698')
        self.canvas.pack()
        #-----------------------------------------------------------------------------

        #property dibawah canvas------------------------------------------------------
        self.text = tk.Label(text='Jumlah Node :')
        self.text.pack()
        self.txBox  = tk.Text(self.root, height = 1, width = 3, bg = "light yellow")
        self.id = []   #inisial id After agar animasi dapat di cancel 
        self.txBox.pack()
        self.btn = tk.Button(text='Buat Graf',command=self.getInput)
        self.btn.pack()
        #-----------------------------------------------------------------------------

        self.root.bind('<Return>', lambda event: self.getInput())
        self.root.mainloop()
    
    def getInput(self):
        inputBox = int(self.txBox.get(1.0,tk.END))
        self.txBox.delete(1.0,tk.END)
        self.canvas.create_rectangle((0,0),(800,490),fill='#b8b698', outline='')
        
        if len(self.id) > 0:
            for id in self.id[::-1]:
                self.root.after_cancel(id)
                self.id.pop(0)
        print(self.id)
        
        self.draw(inputBox)
        print(inputBox)
     

    def window(self):
        w = 800 
        h = 600 

        # get screen width and height
        ws = self.root.winfo_screenwidth() #
        hs = self.root.winfo_screenheight() 

        x = (ws/2) - (w/2) 
        y = (hs/2) - (h/2) - 50
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root.title('Animasi Graph Complex')

    def draw(self, nVertex: int):
        vertices : Hash_Table  = generateVertex(nVertex,700,480)
        print(vertices)
        g : Graph = Graph(vertices)
        g.build_complex_graph()


        
        #--------draw vertex-----------------------------------------
        i = len(g.vertices)
        waktu = 350
        for key,val in iterate_table(g.vertices):
            idVertex_after = self.canvas.after(waktu*i,self.draw_vertex, val)
            self.id.append(idVertex_after)
            i-=1
        #------------------------------------------------------------
        
        #---------draw edge-------------------------------------------
        waktu2 = waktu * len(g.vertices) 
        drawed_key = []  #panjang list val dari tiap key
        t = 1
        for key,val in iterate_table(g.graph):
            drawed_key.append(key)
            for vertex in val:
                if vertex not in drawed_key:  
                    idEdge_after = self.canvas.after(waktu2+(350*t),self.draw_edge,key,vertex)                
                    self.id.append(idEdge_after)
                    t+=1
                    
        #------------------------------------------------------------
        print(self.id)
        g.reset()
    def draw_vertex(self, vertex : Vertex):
        self.canvas.create_oval((vertex.x-10,vertex.y-10),(vertex.x+10,vertex.y+10), fill='red')

    def draw_edge(self, vertex1: Vertex, vertex2: Vertex):
        self.canvas.create_line((vertex1.x,vertex1.y),(vertex2.x,vertex2.y))




if __name__ == '__main__':
    MyApp()


