from scipy import fftpack
import numpy as np
from PIL import Image, ImageDraw, ImageOps
import imageio
import matplotlib.pyplot as plt


def bandReject(image1):
    if len(np.shape(image1)) == 2:
        print("GrayScale")
        # convert image to numpy array
        r_np0 = np.array(image1)

        # fft of image
        r_f_t = fftpack.fftshift(fftpack.fft2(r_np0))

        # Create a low pass filter image
        x = r_np0.shape[1]
        y = r_np0.shape[0]

        # size o circle
        e_x, e_y = 100, 100
        e_x1, e_y1 = 40, 40
        # create a box
        pos_1 = ((x / 2) - (e_x / 2), (y / 2) - (e_y / 2), (x / 2) + (e_x / 2), (y / 2) + (e_y / 2))
        pos_2 = ((x / 2) - (e_x1 / 2), (y / 2) - (e_y1 / 2), (x / 2) + (e_x1 / 2), (y / 2) + (e_y1 / 2))

        band_reject = Image.new("L", (x, y), color=1)
        draw1 = ImageDraw.Draw(band_reject)
        draw1.ellipse(pos_1, fill=0)
        draw1.ellipse(pos_2, fill=1)
        band_bus_np = np.array(band_reject)
        plt.imshow(band_reject)
        plt.show()
        # multiply both the images
        filtered0 = np.multiply(r_f_t, band_bus_np)

        # inverse fft
        inv_image0 = np.uint8(np.abs(np.clip(fftpack.ifft2(fftpack.ifftshift(filtered0)), a_min=0, a_max=255)))

        # multiply 3 channels
        output_image = Image.new("L", image1.size)
        image_draw = ImageDraw.Draw(output_image)
        for x in range(0, image1.height - 1):
            for y in range(0, image1.width - 1):
                image_draw.point((y, x), (int((inv_image0[x, y]))))
        imageio.imsave("oo.jpg", output_image)
        # show
        output_image.show()
    elif len(np.shape(image1)) == 3:
        print("RGB")
        image1.show()
        im1 = Image.Image.split(image1)
        red_image = im1[0]
        green_image = im1[1]
        blue_image = im1[2]

        # convert image to numpy array
        r_np0 = np.array(red_image)
        g_np1 = np.array(green_image)
        b_np2 = np.array(blue_image)

        # fft of image
        r_f_t = fftpack.fftshift(fftpack.fft2(r_np0))
        g_f_t = fftpack.fftshift(fftpack.fft2(g_np1))
        b_f_t = fftpack.fftshift(fftpack.fft2(b_np2))

        # Create a low pass filter image
        x = r_np0.shape[1]
        y = r_np0.shape[0]

        # size o circle
        e_x, e_y = 90, 90
        e_x1, e_y1 = 40, 40
        # create a box
        pos_1 = ((x / 2) - (e_x / 2), (y / 2) - (e_y / 2), (x / 2) + (e_x / 2), (y / 2) + (e_y / 2))
        pos_2 = ((x / 2) - (e_x1 / 2), (y / 2) - (e_y1 / 2), (x / 2) + (e_x1 / 2), (y / 2) + (e_y1 / 2))

        band = Image.new("L", (x, y), color=1)

        draw1 = ImageDraw.Draw(band)
        draw1.ellipse(pos_1, fill=0)
        draw1.ellipse(pos_2, fill=1)
        band_reject_np = np.array(band)
        band.show()

        # multiply both the images
        filtered0 = np.multiply(r_f_t, band_reject_np)
        filtered1 = np.multiply(g_f_t, band_reject_np)
        filtered2 = np.multiply(b_f_t, band_reject_np)
        # inverse fft
        inv_image0 = fftpack.ifft2(fftpack.ifftshift(filtered0))
        inv_image1 = fftpack.ifft2(fftpack.ifftshift(filtered1))
        inv_image2 = fftpack.ifft2(fftpack.ifftshift(filtered2))
        # muliply 3 channels
        output_image = Image.new("RGB", image1.size)
        image_draw = ImageDraw.Draw(output_image)
        for x in range(0, image1.height - 1):
            for y in range(0, image1.width - 1):
                image_draw.point((y, x), (int((inv_image0[x, y])), int((inv_image1[x, y])), int((inv_image2[x, y]))))
        imageio.imsave("C:/Users/dell/PycharmProjects/computer vision project/New folder/Filter.jpg", output_image)
        # show
        output_image.show()
