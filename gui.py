import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import cv2
import random
import os
import featureExtraction as fe
import featureMatching as fm
from PIL import ImageTk, Image
from functools import partial

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
        master.geometry("1000x500")
        self.configure(background="#455A64")
        label1 = tk.Label(self, text="FACE RECOGNITION", font=("Calibri 20 bold"),fg="#80CBC4",bg="#455A64",pady=10)
        label1.grid(row=0,column=0,columnspan=3)

        label2 = tk.Label(self, text="Choose a method: ",background="#455A64",font=("Roboto 8"))
        label2.grid(row=5, column=0, sticky="w")

        button1 = tk.Button(self, text="Euclidean Distance", font=("Roboto 10"),command=lambda:master.switch_frame(eucliMethod), width=20,background="#B0BEC5").grid(row=6, column=0, padx=10)
        button2 = tk.Button(self, text="Cosine Similarity", font=("Roboto 10"),command=lambda:master.switch_frame(cosMethod), width=20,background="#B0BEC5").grid(row=6, column=2,padx=10)

        self.labelFrame = ttk.LabelFrame(self)
        self.button()
        self.grid_columnconfigure(0, minsize=16)

    def button(self):
        #Browse file button
        self.button = ttk.Button(self, text= "Browse A File", command= self.fileDialog(eucliMethod, cosMethod))
        self.button.grid(row = 4, column = 0, columnspan=3, pady=30)
    
    def fileDialog(self,eucliMethod, cosMethod):
        #Command after button clicked
        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype = (("jpeg files","*.jpg"),("all files","*.*")) )
        self.label = ttk.Label(self.labelFrame, text = "")
        self.label.grid(column = 7, row = 1)

        #When image is shown before, image will be destroyed 
        if self.img is not None:
            self.img.destroy()
        
        #When filename is not None, it will call showImage
        if self.filename is not None:
            eucliMethod.sample.append(self.filename)
            cosMethod.sample.append(self.filename)
            eucliMethod.count += 1
            cosMethod.count += 1
            self.showImage(self.filename)

class eucliMethod(tk.Frame):
    pic = 0
    mark = 0
    count = -1
    database_path = 'resources/database/'
    query_path = 'resources/query/'

    ma = None

    database_images = [os.path.join('resources/database/', p) for p in sorted(os.listdir('resources/database/'))]
    query_images = [os.path.join('resources/query/', p) for p in sorted(os.listdir('resources/query/'))]

    sample = []
    img = None

    names_cosine = None 
    match_cosine = None
    img_arr = None
    im = None

    
    def nexts(self):
        self.pic= (self.pic+1) % 5
        self.img_arr = mpimg.imread(os.path.join(self.database_path, self.names_cosine[self.pic]))
        self.im = Image.open(os.path.join(self.database_path, self.names_cosine[self.pic]))
        
        #It will destroy image
        if self.img is not None:
            self.img.destroy()

        #Show image
        tkimage = ImageTk.PhotoImage(self.im)
        self.img = Button(self, bg="#B0BEC5", image=tkimage, command=os.path.join(self.database_path, self.names_cosine[self.pic]))
        self.img.image=tkimage
        self.img.pack()

        k = self.match_cosine[self.pic-1]
        kD = float(k)
        kD *= 100
        
        self.label1.configure(text="{0:.3f}".format(kD)+"%", font=("Calibri 20 bold"), fg="#80CBC4", bg="#455A64", pady=10)

    def prev(self):
        self.pic= (self.pic-1) % 5
        self.img_arr = mpimg.imread(os.path.join(self.database_path, self.names_cosine[self.pic]))
        self.im = Image.open(os.path.join(self.database_path, self.names_cosine[self.pic]))
        
        #It will destroy image
        if self.img is not None:
            self.img.destroy()

        #Show image
        tkimage = ImageTk.PhotoImage(self.im)
        self.img = Button(self, bg="#B0BEC5", image=tkimage, command=os.path.join(self.database_path, self.names_cosine[self.pic]))
        self.img.image=tkimage
        self.img.pack()

        k = self.match_cosine[self.pic-1]
        kD = float(k)
        kD *= 100

        self.label1.configure(text="{0:.3f}".format(kD)+"%", font=("Calibri 20 bold"), fg="#80CBC4", bg="#455A64", pady=10)

    def __init__(self, master):
        master.geometry("500x500")
        # self.configure(background="#455A64")
        self.ma = fm.Matcher('features.json')
        print(self.sample)
        self.names_cosine, self.match_cosine = self.ma.match_euclidean_similarity(self.sample[self.count], topn=5)
        tk.Frame.__init__(self, master)
        master.configure(background="#455A64")
        self.configure(bg="#455A64")


        label = tk.Label(self, text="Euclidean Distance")
        label.pack(pady=10, padx=10)
        label.configure(bg="#455A64", fg="#80CBC4")

        button1 = tk.Button(self, text="Prev", command=self.prev)
        button1.pack()
        button1.configure(background="#B0BEC5")

        button2 = tk.Button(self, text="Next", command=self.nexts)
        button2.pack()
        button2.configure(background="#B0BEC5")

        button3 = tk.Button(self, text="Back to The Start Page", command=lambda: master.switch_frame(StartPage))
        button3.pack()
        button3.configure(background="#B0BEC5")

        self.label1 = tk.Label(self, text="Match", font=("Calibri 20 bold"), fg="#80CBC4", bg="#455A64", pady=10)
        self.label1.pack()

class cosMethod(tk.Frame):
    pic = 0
    mark = 0
    count = -1
    database_path = 'resources/database/'
    query_path = 'resources/query/'

    ma = None

    database_images = [os.path.join('resources/database/', p) for p in sorted(os.listdir('resources/database/'))]
    query_images = [os.path.join('resources/query/', p) for p in sorted(os.listdir('resources/query/'))]

    sample = []
    img = None

    names_cosine = None 
    match_cosine = None
    img_arr = None
    im = None

    def nexts(self):
        self.pic= (self.pic+1) % 5
        self.img_arr = mpimg.imread(os.path.join(self.database_path, self.names_cosine[self.pic]))
        self.im = Image.open(os.path.join(self.database_path, self.names_cosine[self.pic]))
        
        #It will destroy image
        if self.img is not None:
            self.img.destroy()

        #Show image
        tkimage = ImageTk.PhotoImage(self.im)
        self.img = Button(self, bg="#B0BEC5", image=tkimage, command=os.path.join(self.database_path, self.names_cosine[self.pic]))
        self.img.image=tkimage
        self.img.pack()
        
        k = self.match_cosine[self.pic-1]
        kD = float(k)
        kD *= 100

        self.label1.configure(text="{0:.3f}".format(kD)+"%", font=("Calibri 20 bold"), fg="#80CBC4", bg="#455A64", pady=10)

    def prev(self):
        self.pic= (self.pic-1) % 5
        self.img_arr = mpimg.imread(os.path.join(self.database_path, self.names_cosine[self.pic]))
        self.im = Image.open(os.path.join(self.database_path, self.names_cosine[self.pic]))
        
        #It will destroy image
        if self.img is not None:
            self.img.destroy()

        #Show image
        tkimage = ImageTk.PhotoImage(self.im)
        self.img = Button(self, bg="#B0BEC5", image=tkimage, command=os.path.join(self.database_path, self.names_cosine[self.pic]))
        self.img.image=tkimage
        self.img.pack()

        k = self.match_cosine[self.pic-1]
        kD = float(k)
        kD *= 100

        self.label1.configure(text="{0:.3f}".format(kD)+"%", font=("Calibri 20 bold"), fg="#80CBC4", bg="#455A64", pady=10)

    def __init__(self, master):
        master.geometry("500x500")
        # self.configure(background="#455A64")
        self.ma = fm.Matcher('features.json')
        print(self.sample)
        self.names_cosine, self.match_cosine = self.ma.match_cosine_similarity(self.sample[self.count], topn=5)
        tk.Frame.__init__(self, master)
        master.configure(background="#455A64")
        self.configure(bg="#455A64")

        label = tk.Label(self, bg="#455A64", fg="#80CBC4", text="Cosine Similarity")
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, bg="#B0BEC5", text="Prev", command=self.prev)
        button1.pack()

        button2 = tk.Button(self, bg="#B0BEC5", text="Next", command=self.nexts)
        button2.pack()

        button3 = tk.Button(self, bg="#B0BEC5", text="Back to The Start Page", command=lambda: master.switch_frame(StartPage))
        button3.pack()

        self.label1 = tk.Label(self, text="Match", font=("Calibri 20 bold"), fg="#80CBC4", bg="#455A64", pady=10)
        self.label1.pack()

if __name__ == "__main__":
    app = faceRecognition()
    app.mainloop()