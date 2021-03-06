# Linear Algebra and Geometry
## Simple Face Recognition Using Python OpenCV (Vector Based)

First and foremost, huge thanks to our lecturer for guiding us through the process of making this program.

<p align="center">
    <img src="https://stei.itb.ac.id/wp-content/uploads/4x6-Ir_-Rinaldi-Munir-MT.jpg" style="box-shadow:2px 4px 5px rgba(0,0,0,0.3)" width="200">
    <br>
    <em>Dr. Ir. Rinaldi Munir, MT.</em>
</div>

This is a program that is being developed by three people:
- Florencia Wijaya (13518020)
- Matthew Kevin Amadeus (13518035)
- Stefanus Stanley Yoga Setiawan (13518122)

This program uses OpenCV, NumPy, and Matplotlib for the calculations and image showing.
This program uses PyInquirer to make the CLI prompts beautiful.
This program also uses Tkinter to make the GUI of this program.

## Quickstart
### Setting up dependencies
To install the dependencies needed, type in as follows:

- To install OpenCV: 
```bash
pip install opencv-python
```
- To install PyInquirer: 
```bash
pip install PyInquirer
```
- To install NumPy: 
```bash
pip install numpy
```
- To install Matplotlib: 
```bash
pip install matplotlib
```

### Using the CLI
Simply run `main.py` by typing
```bash
python main.py
```
### Using the GUI
Simply run `gui.py` by typing
```bash
python gui.py
```
### Using the face recognition
1. Make a folder called `resources` in the root directory.
2. Make two folders inside, `query` and `database`.
3. Put the images in the two folders, depending on what you want the image to be (as a query, or as a database).