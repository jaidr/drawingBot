# drawingBot
This project is meant to simplify the process of quick and accurate transfer of a drawing with a given image input on nft trading cards created by a web game.
# This is my first coding project
# It was designed as way to reduce the human involvement from sketching on an overly simplified web interface
# Utilizing python's pyautogui, numpy, and cv2, I first take a given reference image as an input and perform image processing (using cv2) to get the neccesary data from the image
# I then use the image data to find what colors from the web toolkit are available and pick the one that is closest
# Using the information of color and location, I can now use pyautogui to utilize this and translate it into the web ui by going to each pixel from top left to bottom right (row by row)
# Ultimately this will result in a pixel to pixel conversion from the input image
# The main issue faced was based on the web ui not being able to handle so many individual strokes
# I attempted to simplify this by creating more simple strokes if the previous pixels color was the same
# This reduced the load on the web ui but does not work as well with more complex images with many colors changing at nearly every couple of pixels
# The next steps would be to implement masks and edge detection using opencv in order to more effectively isolate the core content of the image to further simplify what needs to be transferred 
