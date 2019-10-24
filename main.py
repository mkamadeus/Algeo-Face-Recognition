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
    
def run():
    images_path = 'resources/images/'

    # Making sorted filename array
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
    # Getting 3 random image for query 
    sample = random.sample(files, 3)
    
    # Extract features
    fe.batch_extractor(images_path)

    # Image matching
    ma = fm.Matcher('features.pck')
    
    for s in sample:
        print('Query image ==========================================')
        show_img(s)
        names, match = ma.match(s, topn=3)
        print('Result images ========================================')
        for i in range(3):
            # we got cosine distance, less cosine distance between vectors
            # more they similar, thus we subtruct it from 1 to get match value
            print('Match %s' % (1-match[i]))
            show_img(os.path.join(images_path, names[i]))

run()