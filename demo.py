from main import *

# Specify location of the PNG or JPG image you want to use here
image = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# In main it will print out all results for simplicity
# From here we will utilize the results to make our decision

image = "./graphs/Graph10.jpg"
main(image)

image = "./graphs/_graph002.jpg"
main(image)

image = "./graphs/_graph005.jpg"
main(image)

# Purposely left like this since each investor/trader can chose their confidence level
# But in the future we can streamline a confidence process
print("\nIf nothing is returned under your graph, that means the algos were not confident in finding that price pattern")