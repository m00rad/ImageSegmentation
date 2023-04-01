from PIL import Image, ImageOps, ImageDraw
import FIlters,ImageSeg


def filtering(kernel, kernel_size,input_image):

    input_image.show()
    pixels = input_image.load()
    outImageWidth = (input_image.size[0] - kernel_size + 2)
    outImageHeight = (input_image.size[1] - kernel_size + 2)
    FilteredImage = Image.new("RGB", (int(outImageWidth), int(outImageHeight)))
    draw = ImageDraw.Draw(FilteredImage)
    for x in range(1, input_image.width - 1):
        for y in range(1, input_image.height - 1):
            acc = [0, 0, 0]
            for a in range(len(kernel)):
                for b in range(len(kernel)):
                    xn = x + a - 1
                    yn = y + b - 1
                    p = pixels[xn, yn]
                    acc[0] += p[0] * kernel[a][b]
                    acc[1] += p[1] * kernel[a][b]
                    acc[2] += p[2] * kernel[a][b]
                    draw.point((x, y), (int(acc[0]), int(acc[1]), int(acc[2])))
    FilteredImage.save("output.jpg")
    FilteredImage.show()
    return FilteredImage


filtered = filtering(FIlters.bilateral, FIlters.bilateralSize)
filtered.show()
