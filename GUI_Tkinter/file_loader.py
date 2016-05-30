#! /usr/bin/env python
# encoding: utf-8

from Tkinter import *
from tkFileDialog import *
import sys, os.path

root = Tk()
root.title("ImageFileOpen")

# global
path_name = ""
image_data = PhotoImage(width=64, height=64)

def load_file():
    global image_data, path_name
    filename = askopenfilename(filetypes=[("ImageFiles", (".gif", ".ppm")), 
                                          ("GIF Files", ".gif"), 
                                          ("PPM Files", ".ppm")], 
                               initialdir=path_name)
    if filename != "":
        path_name = os.path.dirname(filename)
        image_data = PhotoImage(file=filename)
        label.configure(image=image_data)

# label
label = Label(root, image=image_data)
label.pack()

# menu
m0 = Menu(root);
root.configure(menu=m0);

m1 = Menu(m0, tearoff=0)
m1.add_command(label="Open", under=0, command=load_file)
m1.add_separator
m1.add_command(label="Exit", under=0, command=sys.exit)
m0.add_cascade(label="File", under=0, menu=m1)

root.mainloop()