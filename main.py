import cv2
import matplotlib.pyplot as plt
import random
import os

import featureExtraction as fe
import featureMatching as fm

def show_img(path):
    img = cv2.imread(path, 1)
    plt.imshow(img)
    plt.show()

os.system('cls')

images_path = 'resources/Database/pins-face-recognition/PINS'

# Making sorted filename array
files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

# Getting 3 random image for query 
sample = random.sample(files, 2)

# Extract features
fe.batch_extractor(images_path)

# Image matching
ma = fm.Matcher('features.pck')
x = int(input('Enter result count: '))

for s in sample:
    print('Query image ==========================================')
    show_img(s)
    names_cosine, match_cosine = ma.match_cosine_similarity(s, topn=x)
    print('Result images ========================================')
    for i in range(x):
        print('Match %s %s' % (match_cosine[i], names_cosine[i]))
        show_img(os.path.join(images_path, names_cosine[i]))
