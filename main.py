from PIL import Image
from ArrayFromPic import ArrayFromPic as afp
#import argparse

def solve(input_file, output_file):
    # Load Image
    print("Loading Image 13")
    im = Image.open(input_file)
    array_from_pic = afp(im)
    print(array_from_pic.mapped_array)
    print('-------------------')
    for row in array_from_pic.mapped_array:
        print(row)
    print(im)

    print("Saving Image 13")
    im = im.convert('RGB')

    im.save(output_file)


# Built in Python argparse used to grab string names from console. To use, uncomment the commented section and comment
# out the hardcoded solve function
def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument("input_file")
    # parser.add_argument("output_file")
    # args = parser.parse_args()
    # # solve(args.input_file, args.output_file)
    solve('graphs/Graph13.jpg', 'output13.jpg')  # comment this out if using argparse



if __name__ == '__main__':
    main()