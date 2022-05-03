import os

from PIL import Image



def imageConverter():
    ss_dir = os.path.dirname(os.path.realpath(__file__)) + '/newImages/'
    graphs_dir = os.path.dirname(os.path.realpath(__file__)) + '/graphs/'
    for id in range(1,9):

        img = Image.open(ss_dir + "sample_0"+str(id)+".png")

        width = img.size[0]
        height = img.size[1]
        '''This assumes that the very first pixel i sthe background color.
        Thus, this background color is compared againsta ny color of the pixel in the Image
        If the background color matches, it is converted to balck RBG(0,0,0)
        Anything that does not match background color is assumed to be a graph,
        thus that graph is converted to WHITE color RBG(255,255,255) '''

        # Get the first pixel
        firstPixel = img.getpixel((0,0))

        for i in range(0,width): # process all pixels
            for j in range(0,height):
                data = img.getpixel((i,j))

                img.putpixel((i,j),(0,0,0)) if data==firstPixel else img.putpixel((i,j),(255,255,255))

        img_to_save = img.convert('RGB')
        img_to_save.save(graphs_dir + "_graph00"+str(id)+".jpg")
        # img.show()