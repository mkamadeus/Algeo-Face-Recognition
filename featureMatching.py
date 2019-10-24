import math
import pickle
import numpy as np
import featureExtraction as fe

class Matcher(object):

    def __init__(self, pickled_db_path="features.pck"):
        # Load pickled feature vector
        with open(pickled_db_path, 'rb') as fp:
            self.data = pickle.load(fp)

        self.names = []
        self.matrix = []
        for k, v in self.data.items():
            self.names.append(k)
            self.matrix.append(v)
        self.matrix = np.array(self.matrix)
        self.names = np.array(self.names)

    def cos_cdist(self, vector):
        # getting cosine distance between search image and images database
        v = vector.reshape(len(vector),1)
        lengthv = 0
        print(len(v))
        for i in range(2048):
            lengthv += v[i]**2
        lengthv = math.sqrt(lengthv)
        a = []
        for i in range(len(self.matrix)):
            b = 0
            w = self.matrix[i].reshape(len(vector),1)
            lengthw = 0
            for j in range(2048):
                lengthw += w[j]**2
                b += v[j]*w[j]
            lengthw = math.sqrt(lengthw)
            c = b/(lengthv*lengthw)
            a.append(1-c)
        a = np.array(a).reshape(-1)
        print(a)
        return a

    def euclidean_distance(self, vector):

        # getting euclidean distance between search image and images database
        dist = []        

        for i in range(15):
            v = vector.reshape(1,-1)
            s = self.matrix[i].reshape(1,-1)
            d = 0
            for j in range (len(v)):
                d += (s[j]-v[j])**2
            dist.append(d**0.5)
        
        dist = np.array(dist)

        return dist

    def match(self, image_path, topn=5):
        features = fe.extract_features(image_path)
        # print(features)
        print(len(features))
        img_distances = self.euclidean_distance(features)
        # print(img_distances)
        print(len(img_distances))
        # getting top 5 records
        nearest_ids = np.argsort(img_distances)[:topn].tolist()
        # print(nearest_ids)
        print(len(nearest_ids))
        nearest_img_paths = [self.names for _,self.names in sorted(zip(nearest_ids,self.names))]
        img_distances = [img_distances for _,img_distances in sorted(zip(nearest_ids,img_distances))]
        # nearest_img_paths = self.names[nearest_ids].tolist()

        return nearest_img_paths, img_distances
    
    def match_cost(self, image_path, topn=5):
        features = fe.extract_features(image_path)
        img_distances = self.cos_cdist(features)
        # getting top 5 records
        nearest_ids = np.argsort(img_distances)[:topn].tolist()
        nearest_img_paths = self.names[nearest_ids].tolist()

        return nearest_img_paths, img_distances[nearest_ids].tolist()