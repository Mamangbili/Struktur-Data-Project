from Graph import Graph, generateVertex
import tkinter as tk
from vertex import Vertex
from Hash_Table import Hash_Table,iterate_table


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
        self.txBox.pack()
        self.btn = tk.Button(text='Buat Graf',command=self.getInput)
        self.btn.pack()
        #-----------------------------------------------------------------------------

        self.root.mainloop()
    
    def getInput(self):
        inputBox = int(self.txBox.get(1.0,tk.END))
        self.txBox.delete(1.0,tk.END)
        self.canvas.create_rectangle((0,0),(800,500),fill='#b8b698')
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
        self.root.title('Animasi Graph')

    def draw(self, nVertex: int):
        vertices : Hash_Table  = generateVertex(nVertex,50,480)
        print(vertices)
        g : Graph = Graph(vertices)
        g.build_complex_graph()

        for key,val in iterate_table(g.graph):
            for vertex in val:
                                            #jari jari 20
                self.canvas.create_oval((vertex.x-10,vertex.y-10),(vertex.x+10,vertex.y+10), fill='red')
                
        
        g.reset()





if __name__ == '__main__':
    MyApp()


