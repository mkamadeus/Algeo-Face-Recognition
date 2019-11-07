import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import featureMatching 
import cv2
import random
import os
import featureExtraction as fe
import featureMatching as fm
from PIL import ImageTk, Image

class faceRecognition(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        #Destroy frame and show new frame
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    filename = None
    img = None

    def showImage(self,filename):
        #Show image from directory
        im = Image.open(filename)
        im = im.resize((300,300), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(im)
        self.img = Button(self, image=tkimage, command=filename)
        self.img.image=tkimage 
        self.img.grid(row=2,column=1)

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.geometry("500x500")
        label = tk.Label(self, text="Choose a method: ")
        label.grid(row=0, column=1)

        self.r = tk.IntVar()
        rbutton1 = tk.Radiobutton(self, text="Euclidean Distance", variable=self.r, value=1, width=20).grid(row=1, column=3)
        rbutton2 = tk.Radiobutton(self, text="Cosine Similarity", variable=self.r, value=2, width=20).grid(row=1, column=4)
        button1 = tk.Button(self, text="OK", command=lambda: master.switch_frame(cosMethod) if self.r==1 else master.switch_frame(eucliMethod), height=1, width=10).grid(row=1, column=5)
        checkbox = tk.Checkbutton(self, text="Randomize Input", width=24).grid(row=1,column=6)

        self.labelFrame = ttk.LabelFrame(self)
        self.button()
        
        self.grid_columnconfigure(0, minsize=16)

    def button(self):
        #Browse file button
        self.button = ttk.Button(self, text= "Browse A File", command= self.fileDialog)
        self.button.grid(column = 1, row = 1)
    
    def fileDialog(self):
        #Command after button clicked
        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype = (("jpeg files","*.jpg"),("all files","*.*")) )
        self.label = ttk.Label(self.labelFrame, text = "")
        self.label.grid(column = 1, row = 2)

        #When image is shown before, image will be destroyed 
        if self.img is not None:
            self.img.destroy()
        
        #When filename is not None, it will call showImage
        if self.filename is not None:
            self.showImage(self.filename)

class eucliMethod(tk.Frame):
    pic = 0
    mark = 0
    images_path = 'resources/query/'
    files = [os.path.join('resources/query/', p) for p in sorted(os.listdir('resources/query/'))]
    sample = random.sample(files,10)
    img = None

    def nexts(self):
        self.pic= (self.pic+1) % 5
        ma = fm.Matcher('features.pck')
        names_cosine, match_cosine = ma.match_cosine_similarity(self.sample[0], topn=5)
        img_arr = mpimg.imread(os.path.join(self.images_path, names_cosine[self.pic]))
        im = Image.open(os.path.join(self.images_path, names_cosine[self.pic]))
        
        #It will destroy image
        if self.img is not None:
            self.img.destroy()

        #Show image
        tkimage = ImageTk.PhotoImage(im)
        self.img = Button(self, image=tkimage, command=os.path.join(self.images_path, names_cosine[self.pic]))
        self.img.image=tkimage
        self.img.pack()

        print(self.pic)

    def prev(self):
        self.pic= (self.pic-1) % 5
        ma = fm.Matcher('features.pck')
        names_cosine, match_cosine = ma.match_cosine_similarity(self.sample[0], topn=5)
        img_arr = mpimg.imread(os.path.join(self.images_path, names_cosine[self.pic]))
        im = Image.open(os.path.join(self.images_path, names_cosine[self.pic]))

        #It will destroy image
        if self.img is not None:
            self.img.destroy()

        #Show Image
        tkimage = ImageTk.PhotoImage(im)
        self.img = Button(self, image=tkimage, command=os.path.join(self.images_path, names_cosine[self.pic]))
        self.img.image=tkimage
        self.img.pack()

        print(self.pic)

    def __init__(self, master):
        master.geometry("500x500")
        tk.Frame.__init__(self, master)

        label = tk.Label(self, text="Euclidean Distance")
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Prev", command=self.prev)
        button1.pack()

        button2 = tk.Button(self, text="Next", command=self.nexts)
        button2.pack()

        button3 = tk.Button(self, text="Back to The Start Page", command=lambda: master.switch_frame(StartPage))
        button3.pack()

class cosMethod(tk.Frame):
    def __init__(self, master):
        master.geometry("500x500")
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Cosine Similarity")
        label.grid(row=1,column=5)

        button1 = tk.Button(self, text="Prev")
        button1.grid(row=5,column=1)

        button2 = tk.Button(self, text="Next")
        button2.grid(row=5,column=10)

        button3 = tk.Button(self, text="Back to The Start Page", command=lambda: master.showFrame(StartPage))
        button3.grid(row=10,column=5)

if __name__ == "__main__":
    app = faceRecognition()
    app.mainloop()