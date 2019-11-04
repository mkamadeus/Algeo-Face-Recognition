import cv2
import matplotlib.pyplot as plt
import random
import os

import featureExtraction as fe
import featureMatching as fm

from consolemenu import *
from consolemenu.items import *

def show_img(path):
    img = cv2.imread(path, 1)
    plt.imshow(img)
    plt.show()

def extractFeatures():
    images_path = 'resources/images/'
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

    # Extract features
    fe.batch_extractor(images_path)
    # Image matching
    ma = fm.Matcher('features.pck')


menu = ConsoleMenu("Main Menu", "Extract Features?")
extractFeaturesMenu = FunctionItem("Yes", extractFeatures)
noExtractFeatures = FunctionItem("No (use available features.pck)2", input, ["pisang"])

menu.append_item(extractFeaturesMenu)
menu.append_item(noExtractFeatures)
menu.show()
# Making sorted filename array


x = int(input('Enter result count: '))

# Getting 3 random image for query 
sample = random.sample(files, 2)
for s in sample:
    print('Query image ==========================================')
    show_img(s)
    names_cosine, match_cosine = ma.match_cosine_similarity(s, topn=x)
    print('Result images ========================================')
    for i in range(x):
        print('Match %s %s' % (match_cosine[i], names_cosine[i]))
        show_img(os.path.join(images_path, names_cosine[i]))
