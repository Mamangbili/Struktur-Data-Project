from Graph import Graph, generateVertex
import tkinter as tk
from vertex import Vertex

root = tk.Tk()
root.geometry('500x500+400+100')

txBox = tk.Text(root, height=2, width=9, bg='light yellow')
txBox.pack()
def getInput():
    inputBox = txBox.get(1.0,"end-1c")
    print('awe')
    label.config(text=inputBox)

btn = tk.Button(root,text='Tampilkan', command=getInput )
btn.pack()

label = tk.Label(root, text='')
label.pack()
root.mainloop()
        