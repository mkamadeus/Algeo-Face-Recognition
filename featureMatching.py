import math
import pickle
import numpy as np
import featureExtraction as fe
<<<<<<< HEAD
import scipy.spatial
import json
=======
import scipy
>>>>>>> user-interface

class Matcher(object):

    def __init__(self, pickled_db_path="features.json"):
        # Load pickled feature vector
        with open(pickled_db_path, 'r') as fp:
            self.data = json.load(fp)

        self.names = []
        self.features = []

        # Convert pickled data to array
        for k, v in self.data.items():
            self.names.append(k)
            self.features.append(v)
        
        # Convert array to NumPy array
        self.names = np.array(self.names)
        self.features = np.array(self.features)

    # Euclidean Similarity Algorithm
    def euclidean_distance(self, vector):
        match_list = []

        query_vector = vector.reshape(len(vector),-1)
        # Normalize vector
        query_norm=0.0
        for i in range(len(query_vector)):
            query_norm+=query_vector[i]**2
        query_norm**=0.5
        query_vector=[x/query_norm for x in query_vector]

        for i in range(len(self.features)):
            database_vector = self.features[i].reshape(len(vector),-1)
            # Normalize vector
            database_norm=0.0
            for i in range(len(database_vector)):
                database_norm+=database_vector[i]**2
            database_norm**=0.5
            database_vector=[x/database_norm for x in database_vector]

            dist = 0.0
            for j in range (len(database_vector)):
                dist += (database_vector[j]-query_vector[j])**2

            match_list.append(1/(1+dist**0.5))
        
        match_list = np.array(match_list).reshape(-1)

        # Returns dist for each comparison
        return match_list

    # Cosine Similarity Algorithm
    def cosine_similarity(self, vector):
        match_list = []

        query_vector = vector.reshape(len(vector),1)

        # Calculate sqrt(sigma(x))
        sqrt_query_sum = 0.0
        for i in range(len(query_vector)):
            sqrt_query_sum += query_vector[i]**2

        sqrt_query_sum**=0.5

        for i in range(len(self.features)):
            
            product_sum = 0.0
            database_vector = self.features[i].reshape(len(vector),1)
            sqrt_database_sum = 0
            for j in range(len(database_vector)):
                sqrt_database_sum += database_vector[j]**2 # Calculate sqrt(sigma(y))
                product_sum += query_vector[j]*database_vector[j] # Calculate sigma(xy)
            sqrt_database_sum **= 0.5
            
            c = product_sum/(sqrt_query_sum*sqrt_database_sum)
            match_list.append(c)

        match_list = np.array(match_list).reshape(-1)
        return match_list


    def match_euclidean_similarity(self, image_path, topn=5):
        # Compare image_path with other images
        features = fe.extract_features(image_path)
        img_distances = self.euclidean_distance(np.array(features))

        # Slice list with len() = topn after sorted descending
        nearest_img_index = np.argsort(img_distances)[::-1][:topn].tolist()
        nearest_img_paths = self.names[nearest_img_index].tolist()

        return nearest_img_paths, img_distances[nearest_img_index].tolist()
            
    def match_cosine_similarity(self, image_path, topn=5):
        # Compare image_path with other images
        features = fe.extract_features(image_path)
        img_distances = self.cosine_similarity(np.array(features))

        # Slice list with len() = topn after sorted descending
        nearest_img_index = np.argsort(img_distances)[::-1][:topn].tolist()
        nearest_img_paths = self.names[nearest_img_index].tolist()

        return nearest_img_paths, img_distances[nearest_img_index].tolist()