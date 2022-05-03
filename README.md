# Quickly-Analyzing-Stock-Charts

## Demo / Presentation
https://docs.google.com/presentation/d/1z0lVNpF1kBAoQu-vx_ps85bKoEdzJO-kbDC3REZXtFw/edit?usp=sharing



## Report
See attached PDF for final project report



## Demo
To demo our code to be more simple, run demo.py

To make sure it can run, please look into how to run



## How to run + use on your end

To run this project, you will need a few libraries.
Make sure to have the following libraries installed via pip:

#### Pillow (use following commands)
- python3 -m pip install --upgrade pip
- python3 -m pip install --upgrade Pillow

##### Numpy

##### Math (should come default)

##### OS (should come default)

##### Time (should come default)


Now that you have all libraries available, you can run the testing.py file to see our results. 
testing.py was where we ran through all items to get results and debug.

If you would like to pass in your own graph (.png or .jpg), use the main function from main.py in any script you are building up.



## Datasets (visual guide in presentation)

#### Graphs 
Graphs contains 15 graphs (6 increasing, 6 decreasing, 3 neutral) in 28x28. 
All graphs were drawn by John, and their label (label.txt) was decided based on the y-value of the last column compared to the first column.

The graphs are extremes to initially create generic algorithms to solve what type of graph we see.

After we tested our base algorithms, we implemented new labels (label_revisit.txt) which were based on pricing patterns we utilized when researching pricing patterns (see usseful links below).
We labeled each graph and changed where we predicted the price would go after (6 increasing, 8 decreasing, 1 neutral)

After our prediction resilts dropped we created new algorithms that attempted to see if they can notice a specific pricing pattern

Accuracy was not great, but the timing was real quick. 
So with this we saw that the pricing pattern algorithms would work on larger graphs that had more clearly defined pricing patterns.


#### newImages
We finally ran all our algorithms on newImages dataset which were 8 screeshots of price fluctuations from commission-free brokers. 
The dataset contained graphs of various colors (sources) which are labeled in Label_latest.txt.
We had 5 graphs that would be positive, 2 negative, and 1 neutral.
These are the labels of where the price was 5 minutes after the screenshot was taken.



## Current State
The current state of the additional algorithms (price pattern focused) is that they need to be a bit more fine tuned.
However, the algorithms do work on larger (wider) graphs. 
What this means is that our algorithms find a pricing pattern that has been happening for longer periods of time.

This is good, but this might result in us being too late to a movement, and therefore missing out on profits. 
With more graphs, testing, and fine tuning, we believe these algorithms can be utilized to generate profits



#### Links we used
- https://www.investopedia.com/articles/technical/112601.asp
- https://stockstotrade.com/chart-patterns/ 
- https://www.elearnmarkets.com/blog/chart-patterns-to-know-trading-stock/ 
- https://www.daytrading.com/patterns 
- https://www.photopea.com/ 
