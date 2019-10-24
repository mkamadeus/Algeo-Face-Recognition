import cv2
import os
import numpy as np
import pickle

# Feature extractor
def extract_features(image_path, vector_size=32):
    # Load image from path, with RGB mode
    image = cv2.imread(image_path, 1)
    try:
        # Using KAZE Algorithm
        alg = cv2.KAZE_create()
        kps = alg.detect(image)

        # Getting 32 dominant feature vectors 
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
        
        # Does calculation to feature vectors
        kps, dsc = alg.compute(image, kps)

        # Flatten feature vector
        dsc = dsc.flatten()
        
        # Making feature vector of same size (64 dimensions)
        needed_size = (vector_size * 64)
        if dsc.size < needed_size:
            # Not enough feature vector, concatenate array of zeros
            dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
    except cv2.error as e:
        print('Error: ', e)
        return None

    return dsc


def batch_extractor(images_path, pickled_db_path="features.pck"):
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

    result = {}
    for f in files:
        print('Extracting features from image %s' % f)
        name = f.split('/')[-1].lower()
        result[name] = extract_features(f)
    
    # Save pickled feature vector
    with open(pickled_db_path, 'wb') as fp:
        pickle.dump(result, fp)