from Graph import Graph, generateVertex
import tkinter as tk
from vertex import Vertex

t = generateVertex(5)
g = Graph(t)

class MyApp:
    def __init__(self):
        self.root = tk.Tk()
        self.window()
        self.canvas = tk.Canvas(width=800, height=500,background='skyblue')
        self.canvas.pack()



        self.text = tk.Label(text='Jumlah Node :')
        self.text.pack()
        self.txBox = tk.Text(self.root, height = 1,
                            width = 3,
                            bg = "light yellow")
        self.txBox.pack()
        
        self.btn = tk.Button(text='Buat Graf')
        self.btn.pack()


        self.root.mainloop()

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

if __name__ == '__main__':
    MyApp()


