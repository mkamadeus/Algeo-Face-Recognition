import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure 

class faceRecognition (tk.Tk):
    def __init__ (self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Face Recognition")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Picture, Method, eucliMethod, cosMethod):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame(Method)

    def showFrame (self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Picture(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        choice1 = tk.Checkbutton(self, text="Random").grid(row=0)
        choice2 = tk.Checkbutton(self, text="Input").grid(row=1)

class Method(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Choose a Method")
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Euclidean Distance", command=lambda: controller.showFrame(eucliMethod))
        button1.pack()

        button2 = ttk.Button(self, text="Cosine Similarity", command=lambda: controller.showFrame(cosMethod))
        button2.pack()

class eucliMethod(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Euclidean Distance")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Prev")
        button1.pack()

        button2 = ttk.Button(self, text="Next")
        button2.pack()

        button3 = ttk.Button(self, text="Back to The Start Page")
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

        button1 = ttk.Button(self, text="Prev")
        button1.pack()

        button2 = ttk.Button(self, text="Next")
        button2.pack()

        button3 = ttk.Button(self, text="Back to The Start Page")
        button3.pack()

master = faceRecognition()
master.mainloop()