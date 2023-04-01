from scipy import fftpack
import numpy as np
from PIL import Image, ImageDraw, ImageOps
import imageio
import matplotlib.pyplot as plt


def Display_Histogram(image):
    len(np.shape(image))
    if len(np.shape(image)) == 2:
        hist_freq = image.histogram()
        hist_index = np.arange(256)
        plt.figure("Gray Image Histogram")
        plt.bar(x=hist_index, height=hist_freq)
        plt.show()
    elif len(np.shape(image)) == 3:
        if np.shape(image)[2] == 3:
            Rimage, Gimage, Bimage = image.split()
            Rhist_freq = Rimage.histogram()
            Ghist_freq = Gimage.histogram()
            Bhist_freq = Bimage.histogram()
            hist_index = np.arange(256)
            plt.figure("Red Channel Histogram")
            plt.bar(x=hist_index, height=Rhist_freq)
            plt.show()
            plt.figure("Green Channel Histogram")
            plt.bar(x=hist_index, height=Ghist_freq)
            plt.show()
            plt.figure("Blue Channel Histogram")
            plt.bar(x=hist_index, height=Bhist_freq)
            plt.show()
        else:
            print("this image type is invalid")
            return
    else:
        print("this image type is invalid")


def EditContrast(EditionValue, mode,path):
    # def EditContrast(image,EditionValue, mode)
    # if it pass the image as a parameter
    image = Image.open(path)
    # Will deleted if image is
    MaxValue = 255
    MinValue = 0
    if mode == "brightness":
        if len(np.shape(image)) == 3:
            output_image = Image.new("RGB", image.size)
            draw = ImageDraw.Draw(output_image)
            for x in range(output_image.width):
                for y in range(output_image.height):
                    red, green, blue = image.getpixel((x, y))
                    red += EditionValue
                    green += EditionValue
                    blue += EditionValue
                    if red > MaxValue:
                        red = MaxValue
                    if green > MaxValue:
                        green = MaxValue
                    if blue > MaxValue:
                        blue = MaxValue
                    draw.point((x, y), (red, green, blue))
            # output_image.show()
            output_image.save("BrightnessImage.jpg")
        elif len(np.shape(image)) == 2:
            output_image = Image.new("L", image.size)
            draw = ImageDraw.Draw(output_image)
            for x in range(output_image.width):
                for y in range(output_image.height):
                    PixlVal = image.getpixel((x, y))
                    PixlVal += EditionValue
                    if PixlVal > MaxValue:
                        PixlVal = MaxValue
                    draw.point((x, y), PixlVal)
            output_image.save("BrightnessImage.png")
    elif mode == "Darkness":
        if len(np.shape(image)) == 3:
            output_image = Image.new("RGB", image.size)
            draw = ImageDraw.Draw(output_image)
            for x in range(output_image.width):
                for y in range(output_image.height):
                    red, green, blue = image.getpixel((x, y))
                    red -= EditionValue
                    green -= EditionValue
                    blue -= EditionValue
                    if red < MinValue:
                        red = MinValue
                    if green < MinValue:
                        green = MinValue
                    if blue < MinValue:
                        blue = MinValue
                    draw.point((x, y), (red, green, blue))
            # output_image.show()
            output_image.save("DarknessImage.jpg")
        elif len(np.shape(image)) == 2:
            output_image = Image.new("L", image.size)
            draw = ImageDraw.Draw(output_image)
            for x in range(output_image.width):
                for y in range(output_image.height):
                    PixlVal = image.getpixel((x, y))
                    PixlVal -= EditionValue
                    if PixlVal < MinValue:
                        PixlVal = MinValue
                    draw.point((x, y), PixlVal)
            output_image.save("DarknessImage.png")
        else:
            print("Invalid Image type !")
            return
    else:
        print("Invalid Mode !")
        return
    output_image.show()
    # return output_image


image1 = Image.open('paint.jpg')
image2 = ImageOps.grayscale(image1)
Display_Histogram(image1)
print("RGB Done")
Display_Histogram(image2)
print("Gray Scale Done")

EditContrast(100, "brightness",'paint.jpg')
EditContrast(100, "Darkness",'paint.jpg')
