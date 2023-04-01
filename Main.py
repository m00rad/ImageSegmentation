import band_reject_filter
import histogramEqualization
import Filter
import seggg
import bright_ImageHistogram
import FIlters
import ImageSeg
import PIL
from PIL import Image,ImageOps
import numpy as np
import math
import random


image = Image.open("Image_with_periodic_noise.jpg")
band_reject_filter.bandReject(image)
histogramEqualization.histogram_equalization(image)
seggg.Kmeans(image)
image = Filter.filtering(FIlters.laplacian,FIlters.laplacianSize,image)
bright_ImageHistogram.Display_Histogram(image)
bright_ImageHistogram.EditContrast(100,"Darkness","17.jpg")


