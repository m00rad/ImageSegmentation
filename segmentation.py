from builtins import range

import numpy as np
from PIL import Image
import matplotlib
import math

image = Image.open("17.jpg")
imageArray = np.array(image)
pixels = image.load()
image.mode = "HSV"


def init_centroids():
    array_one_d = imageArray.flatten()
    k = 3
    centroid_pValue = []
    centroid_pos = []
    for x in range(0, k):
        centroid_pValue.append(np.random.choice(array_one_d, (1, 3)))
        centroid_pos.append((np.random.randint(0, image.size[0] + 1), np.random.randint(0, image.size[1] + 1)))
    return centroid_pValue, centroid_pos, k


def assignPoints(image_array, centroids, k):
    data = []
    for j in range(0, k):
        data.append([])
    for x in range(0, image.width):
        for y in range(0, image.height):
            print(image_array[x, y])
            dist = []
            for j in range(0, k):
                subtract = np.abs(np.subtract(image_array[x, y], centroids[j]))
                d = math.sqrt(np.sum(subtract))
                dist.append(d)
            centr_idx = dist.index(min(dist))
            data[centr_idx].append(image_array[x, y])
            print(data[centr_idx][0])
            for i in dist:
                print(i)
            print(centr_idx)


returned = init_centroids()
centroid = returned[0]
clusters = returned[2]

assignPoints(imageArray, centroid, clusters)
