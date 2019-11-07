import cv2
import matplotlib.pyplot as plt
import random
import os
from tkinter import filedialog
from tkinter import *

import promptInput as pi
import featureExtraction as fe
import featureMatching as fm

def showImage(path):
    img = cv2.imread(path, 0)
    cv2.imshow(path, img)
    cv2.waitKey()

def printAsPercentage(val):
    print('Match : ',end='')
    print(round(val*100,2),end='')
    print('%')

<<<<<<< HEAD
def printAsDecimal(val):
    print('Match : ',end='')
    print(round(val,4))
=======
images_path = 'resources/Database/pins-face-recognition/PINS'
>>>>>>> user-interface

settings = pi.promptInput()
database_path = 'resources/database/'
query_path = 'resources/query/'

database_images = [os.path.join(database_path, p) for p in sorted(os.listdir(database_path))]
query_images = [os.path.join(query_path, p) for p in sorted(os.listdir(query_path))]

if(settings['extract_database']):
    # Extract features to features.pck
    fe.batch_extractor(database_path)

# Image matching
ma = fm.Matcher('features.json')


# Getting random images for query 
sample = []
if(settings['randomize']==True):
    sample = random.sample(query_images, 1)
else:
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    sample = [root.filename]
    root.destroy()

# Setting threshold
threshold = 0.0
if(settings['comparison_mode']=='strict'):
    threshold=0.7
elif(settings['comparison_mode']=='loose'):
    threshold=0.5

for s in sample:
    print('Query image: ')
    showImage(s)
    names, match = [], []
    if(settings['similarity_method']=='euclidean'):
        names, match = ma.match_euclidean_similarity(s, topn=settings['result_count'])
    elif(settings['similarity_method']=='cosine'):
        names, match = ma.match_cosine_similarity(s, topn=settings['result_count'])

    print('Result images: ')
    for i in range(settings['result_count']):
        print('#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#')
        if(settings['output_mode']=='percentage'):
            printAsPercentage(match[i])
        elif(settings['output_mode']=='decimal'):
            printAsDecimal(match[i])

        print('Filename : ', end='')
        print(names[i])

        print('Does image match? : ', end='')
        if(match[i]>=threshold):
            print('YES')
        else:
            print('NO')

        # Show image in directory
        showImage(os.path.join(database_path, names[i]))
