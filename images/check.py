from PIL import Image

im = Image.open('bg2.jpg')
width, height = im.size

print(width)
print(height)

im = Image.open('IMG_1800.jpg')
width, height = im.size

print(width)
print(height)

im = Image.open('IMG_1801.jpg')
width, height = im.size

print(width)
print(height)