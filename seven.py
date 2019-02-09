"""
     challenge seven.
     http://www.pythonchallenge.com/pc/def/oxygen.html
"""
import urllib3
from PIL import Image, ImageColor
import numpy as np

def take_in_data(url):
    http = urllib3.PoolManager()
    return http.request("GET", url)

def get_pixel(image, i, j):
    # Inside image bounds?
    width, height = image.size
    if i > width or j > height:
        return None
    # Get Pixel
    pixel = image.getpixel((i, j))
    return pixel

if __name__ == "__main__":
    web_data = take_in_data("http://www.pythonchallenge.com/pc/def/oxygen.png")
    image_path = "oxygen.png"
    original = Image.open(image_path)
    #original.show()
    w, h = original.size
    grey_pixels = []
    for i in range(w):
        for j in range(h):
            pixel = original.getpixel((i, j))
            if sum(pixel) < 100:
                grey_pixels.append(pixel)
    data = original.getdata()
    #print(list(data))
    data = list(data)
    line = []
    for i, pixel in enumerate(data):
        if pixel[0] == pixel[1] and pixel[1] == pixel[2]:
            line.append(pixel)

    #print('*'*40)
    #print('\n')
    code = ''
    for i in line:
        code += code.join(chr(i[0]))
    #print(code)
    # extracted that the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121] visually
    secret = ''.join(chr(i) for i in [105, 110, 116, 101, 103, 114, 105, 116, 121])
    print('!'*50)
    print(secret)
    print('!'*50)
    # integrity!!!
