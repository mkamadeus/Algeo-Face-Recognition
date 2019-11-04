import cv2
import matplotlib.pyplot as plt
import random
import os

import featureExtraction as fe
import featureMatching as fm

from consolemenu import *
from consolemenu.screen import *
from consolemenu.items import *
from consolemenu.prompt_utils import *

def show_img(path):
    img = cv2.imread(path, 1)
    plt.imshow(img)
    plt.show()

images_path = 'resources/images/'
files = []
files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
ma = fm.Matcher()

def extractFeatures():
    global files
    global ma
    global images_path

    # Extract features
    fe.batch_extractor(images_path)
    # Image matching
    ma = fm.Matcher('features.pck')
    exit()

method=-1
def setMethod(x):
    global method
    method=x
    exit()

result=-1
def setResult(x):
    global result
    result=x
    exit()

# Extract Features Menu
menu = ConsoleMenu("Face Recognition", "Extract Features?", show_exit_option=False)

option1 = FunctionItem("Yes", extractFeatures)
option2 = FunctionItem("No", exit)

menu.append_item(option1)
menu.append_item(option2)

menu.show()


menu2 = ConsoleMenu("Similarity Method", "Choose Similarity Method: ", show_exit_option=False)

option1 = FunctionItem("Euclidean Similarity", setMethod, [1])
option2 = FunctionItem("Cosine Similarity", setMethod, [2])

menu2.append_item(option1)
menu2.append_item(option2)

menu2.show()

s = Screen()
s._screen_height = 10
s._screen_width = 10
result = int(s.input("Input Result Count: "))
s.clear()

# Getting 3 random image for query 
sample = random.sample(files, 1)
for s in sample:
    print('Query image ==========================================')
    show_img(s)
    names_cosine, match_cosine = ma.match_cosine_similarity(s, topn=result)
    print('Result images ========================================')
    for i in range(result):
        print('Match %s %s' % (match_cosine[i], names_cosine[i]))
        show_img(os.path.join(images_path, names_cosine[i]))
