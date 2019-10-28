import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
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

        button1 = ttk.Button(self, text="OK", command=lambda: controller.showFrame(eucliMethod) if r==1 else controller.showFrame(cosMethod)).grid(row=2, column=3)
        checkbox = tk.Checkbutton(self, text="Randomize Input", width=24).grid(row=4,column=3)

        self.grid_columnconfigure(0, minsize=16)

#class Picture(tk.Frame):
#   def __init__ (self, parent, controller):
#        tk.Frame.__init__(self, parent)
#        choice1 = tk.Checkbutton(self, text="Random").grid(row=0)
#        choice2 = tk.Checkbutton(self, text="Input").grid(row=1)

#class Method(tk.Frame):
#    def __init__ (self, parent, controller):
#        tk.Frame.__init__(self, parent)
#        label = tk.Label(self, text="Choose a Method")
#        label.pack(pady=10,padx=10)

#        button1 = ttk.Button(self, text="Eulidean Distance", command=lambda: controller.showFrame(eucliMethod))
#        button1.pack()

#       button2 = ttk.Button(self, text="Cosine Similarity", command=lambda: controller.showFrame(cosMethod))
#        button2.pack()

class eucliMethod(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Euclidean Distance")
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Prev").pack()

        button2 = tk.Button(self, text="Next")
        button2.pack()

        button3 = tk.Button(self, text="Back to The Start Page", command=lambda: controller.showFrame(Start))
        button3.pack()

        #f = Figure(figsize=(5,5), dpi=100)
        #a = f.add_subplot(111)

        #canvas = FigureCanvasTkAgg(f, self)
        #canvas.show()
        #canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        #toolbar = NavigationToolbar2TkAgg (canvas, self)
        #toolbar.update()
        #canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

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