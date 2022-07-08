import os
from PIL import Image, ImageDraw


def imagereader(image):
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    reds = pix[0, 0][0]
    greens = pix[0, 0][1]
    blues = pix[0, 0][2]
    draw = ImageDraw.Draw(image)
    if reds == blues and blues == greens and greens == 233:
        imageconverter(draw, width, height, pix, True)
    elif reds == blues and blues == greens and greens == 255:
        imageconverter(draw, width, height, pix, False)


def imageconverter(draw, width, height, pix, mode):
    if mode:
        for i in range(width):
            for j in range(height):
                redn = pix[i, j][0]
                greenn = pix[i, j][1]
                bluen = pix[i, j][2]
                if redn > 233 and greenn > 233 and bluen > 233:
                    draw.point((i,j), (233, 233, 233))
    else:
        for i in range(width):
            for j in range(height):
                redn = pix[i, j][0]
                greenn = pix[i, j][1]
                bluen = pix[i, j][2]
                if redn >= 235 and greenn >= 235 and bluen >= 235 and redn != 255 and greenn != 255 and bluen != 255:
                    draw.point((i, j), (255, 255, 255))


dir = r'dir'
for file in os.listdir(dir):
    path = os.path.join(dir, file)
    if ".png" in path:
        image = Image.open(path)
        imagereader(image)
        image.save(path, "png")
