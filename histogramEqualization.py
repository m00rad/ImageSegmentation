from PIL import Image,ImageOps


def histogram_equalization(inputImage):
    inputImage = ImageOps.grayscale(inputImage)
    outputImage = Image.new('L', inputImage.size)

    width, height = inputImage.size

    frequency = {}

    for intensity in range(256):
        frequency[intensity] = 0

    for x in range(width):
        for y in range(height):
            intensity = inputImage.getpixel((x, y))

            if intensity in frequency:
                frequency[intensity] += 1
            else:
                frequency[intensity] = 1

    intensityFrequencies = [frequency[key] for key in sorted(frequency.keys())]

    cummulativeSum = 0
    index = 0

    cdf = []
    for intensityFrequency in intensityFrequencies:
        cummulativeSum += intensityFrequency
        cdf.append(cummulativeSum)
        index += 1

    minCDF = cdf[0]
    maxCDF = cdf[-1]

    normalizedCDF = []

    for value in cdf:
        normalizedCDF.append(((value - minCDF) * 255) / (maxCDF - minCDF))

    for x in range(width):
        for y in range(height):
            intensity = inputImage.getpixel((x, y))
            outputPixel = int(normalizedCDF[intensity])
            outputImage.putpixel((x, y), outputPixel)

    outputImage.save('histogramEqualization.jpg')
    outputImage.show()
