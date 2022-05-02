from PIL import Image
import numpy as np

# Import the source image
input_image = Image.open("newImages/image1.png")
newsize = (28, 28)
input_image = input_image.resize(newsize)
#pix = input_image.load()

#input_image.size[0]
#print(input_image.size[0])
w = input_image.size[0]
h = input_image.size[1]

mapped_array = np.zeros((w, h))
print(mapped_array)
data = list(input_image.getdata(1))

for i in range(w):
    for j in range(h):
        data1 = input_image.getpixel((i,j))
        #print(data1)


print("-------------")
print(data)