import tkinter as tk
from tkinter import ttk
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Reference : How to Embed a Matplotlib Graph to Your TkInter GUI 
# (https://pythonprogramming.net/how-to-embed-matplotlib-graph-tkinter-gui/)

class faceRecognition (tk.Tk):
    def __init__ (self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Face Recognition")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Start, eucliMethod, cosMethod):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame(Start)

    def showFrame (self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Start(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Choose a method: ")
        label.grid(row=0, column=1)

        r = tk.IntVar()
        rbutton1 = ttk.Radiobutton(self, text="Euclidean Distance", variable=r, value=1, width=20).grid(row=2, column=1)
        rbutton2 = ttk.Radiobutton(self, text="Cosine Similarity", variable=r, value=2, width=20).grid(row=3, column=1)
        which_button_is_selected = r.get()
        print(which_button_is_selected)

        button1 = ttk.Button(self, text="OK", command=lambda: controller.showFrame(eucliMethod) if (which_button_is_selected)==1 else controller.showFrame(cosMethod))
        button1.grid(row=2, column=3)

        checkbox = tk.Checkbutton(self, text="Randomize Input", width=24)
        checkbox.grid(row=4,column=3)

        self.grid_columnconfigure(0, minsize=16)

class Browse(tk.Frame):
    def __init__(self):
        super(Browse, self).__init__()
        self.minsize(640,400)

        labelFrame = ttk.LabelFrame(self, text="Choose a Picture")
        labelFrame.grid(row=1, column=1, padx=20, pady=20)

    def buttonToBrowse(self):
        button1 = ttk.Button(self, text="Browse File",command=self.fileBrowse())
        button1.grid(row=2,column=1)

    def fileBrowse(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetype=(("jpeg","*.jpg"), ("All Files", "*.*")))
        label = ttk.Label(labelFrame, text="")
        label.grid(row=2, column=2)
        label.configure(text=filename)

class eucliMethod(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Euclidean Distance")
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Prev")
        button1.pack()

        button2 = tk.Button(self, text="Next")
        button2.pack()

        button3 = tk.Button(self, text="Back to The Start Page", command=lambda: controller.showFrame(Start))
        button3.pack()

        img_arr = mpimg.imread('resources/images/pins-face-recognition/PINS/pins_Aaron Paul/Aaron Paul0_262.jpg')
        
        f = Figure()
        a = f.add_subplot(111)
        a.imshow(img_arr)

        canvas = FigureCanvasTkAgg(f, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack()

class cosMethod(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Cosine Similarity")
        label.grid(row=1,column=5)

        button1 = ttk.Button(self, text="Prev")
        button1.grid(row=5,column=1)

        button2 = ttk.Button(self, text="Next")
        button2.grid(row=5,column=10)

        button3 = ttk.Button(self, text="Back to The Start Page", command=lambda: controller.showFrame(Start))
        button3.grid(row=10,column=5)

master = faceRecognition()
master.mainloop()