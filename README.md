# **Finding Lane Lines on the Road** 

The goal of this project is to find lane lines on the road. The result was tested first on image and then on video.

### Reflection
The steps involved in the pipeline were:
1. Convert an image to grayscale. 
2. Apply Gaussian Blurr to reduce image detail and noise.
3. Apply Canny edge detection to detect edges in an image.
4. Mask an area of interest
5. Mark straight line using hough transformation
6. Segment left and right lanes using slope (Left lane lines have negative slope, Right lane lines have positive slope.)
7. Extend a line of best fit through left and right lane line points.


### 2. Identify potential shortcomings with your current pipeline
Shortcomings with my current pipeline is as follow:
1. The extended line through segmented lane lines is very shaky.

### 3. Suggest possible improvements to your pipeline
One possible improvement would be to increase frame per second(fps) in the video.
The other possible solution would be to decrease the lenght of the extended lines.
