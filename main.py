import cv2
import matplotlib.pyplot as plt
import random
import os

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

def printAsDecimal(val):
    print('Match : ',end='')
    print(round(val,4))


settings = pi.promptInput()
images_path = 'resources/images/'
files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

if(settings['extract_database']):
    # Extract features to features.pck
    fe.batch_extractor(images_path)

# Image matching
ma = fm.Matcher('features.pck')

# Getting random images for query 
sample = random.sample(files, 1)

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
        showImage(os.path.join(images_path, names[i]))
