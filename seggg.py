from PIL import Image
import numpy as np
import math
import random
import bright_ImageHistogram


def Kmeans(im):
    imageArray = np.array(im)
    pix = im.load()
    im.show()
    row = im.size[1]
    col = im.size[0]
    K_m = 15
    number_test = 0
    pic = np.zeros((col, row), dtype=int)
    summ = np.zeros((K_m, 3), dtype=int)
    num = np.zeros((K_m,), dtype=int)
    photo = np.zeros((row, col, 3), dtype=np.uint8)
    array_one_d = imageArray.flatten()
    cluster = []
    compare = []
    for x in range(0, K_m):
        cluster.append(np.random.choice(array_one_d, (1, 3)))
        compare.append(np.random.choice(array_one_d, (1, 3)))
    subtract = np.zeros((3, 1), dtype=int)
    distance = np.zeros((K_m,))
    while number_test == 0:
        # take values before change it
        for k in range(K_m):
            compare[k] = cluster[k]
        for i in range(row):
            for j in range(col):
                for k in range(K_m):
                    subtract = np.subtract(pix[j, i], cluster[k])
                    distance[k] = np.sqrt(np.inner(subtract, subtract))
                dis = distance.argmin()
                pic[j, i] = dis
        for i in range(row):
            for j in range(col):
                for k in range(K_m):
                    if pic[j, i] == k:
                        summ[k] += pix[j, i]
                        num[k] += 1
        for i in range(K_m):
            # if num[i] != 0 :
            summ[i] = (summ[i] / num[i])
            summ[i] = np.floor(summ[i])
            cluster[i] = summ[i]

            number_test = 1

    for i in range(row):
        for j in range(col):
            for k in range(K_m):
                if pic[j, i] == k:
                    photo[i, j] = cluster[k]
    img = Image.fromarray(photo)
    img.save('myimg.jpg')
    img.show()
