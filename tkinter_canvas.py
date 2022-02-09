#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from tkinter import *

# init tk
root = Tk()
root.geometry("+100+100")

# create canvas
myCanvas = Canvas(root, bg="white", height=800, width=800, )


# draw arcs
coord = 10, 10, 300, 300
arc = myCanvas.create_arc(coord, start=0, extent=150, fill="red")
arv2 = myCanvas.create_arc(coord, start=150, extent=215, fill="green")

# add to window and show
myCanvas.pack()
root.mainloop()
