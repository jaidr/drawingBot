import pyautogui as pg
import cv2
import numpy as np
import keyboard
import math
# Press Shift+F10 to execute it or replace it with your code.
# print(pg.position())

# asking user what frame they are using
# frame = input("What frame are you using: ")
# used to find size of drawing area
# frameList = ["magitor","interface","easel","explosion","bunny paws"]
# fix this to be accurate
# drawingArea = ["100x100","150x100","100x80","80x100","90x90"]
# size = drawingArea[ frameList.index(frame)]
# print(frame + " " + size)

#frame dimensions
def bunny_Paws():
    return 858, 400, 1058, 720, 200, 315
def ed1_Default():
    return 858, 449, 1058, 651, 200, 202

# defining vars using frame
topLeftX,topLeftY,botRightX,botRightY,width,height = ed1_Default()


# full color palate
allColors = [[0,0,0] , [19,19,19] , [27,27,27] , [39,39,39] , [61,61,61] , [93,93,93] , [133,133,133] , [180,180,180] , [255,255,255] , [199,207,221] , [146,161,185] , [101,115,146] , [66,76,110] , [42,47,78] , [26,25,50] , [14,7,27] , [28,18,28] , [57,31,33] , [93,44,40] , [138,72,54] , [191,111,74] , [230,156,105] , [246,202,159] , [249,230,207] , [237,171,80] , [224,116,56] , [198,69,36] , [142,37,29] , [255,80,0] , [237,118,20] , [255,162,20] , [255,200,37] , [255,235,87] , [211,252,126] , [153,230,95] , [90,197,79] , [51,152,75] , [30,111,80] , [19,76,76] , [12,46,68] , [0,57,109] , [0,105,170] , [0,152,220] , [0,205,249] , [12,241,255] , [148,253,255] , [253,210,237] , [243,137,245] , [219,63,253] , [122,9,250] , [48,3,217] , [12,2,147] , [3,25,63] , [59,20,67] , [98,36,97] , [147,56,143] , [202,82,201] , [200,80,134] , [246,129,135] , [245,85,93] , [234,50,60] , [196,36,48] , [137,30,43] , [87,28,39]]
# colorsRow1 = [[0,0,0] , [19,19,19] , [27,27,27] , [39,39,39] , [61,61,61] , [93,93,93] , [133,133,133] , [180,180,180] , [255,255,255] , [199,207,221] , [146,161,185] , [101,115,146] , [66,76,110] , [42,47,78] , [26,25,50] , [14,7,27]]
# colorsRow2 = [[28,18,28] , [57,31,33] , [93,44,40] , [138,72,54] , [191,111,74] , [230,156,105] , [246,202,159] , [249,230,207] , [237,171,80] , [224,116,56] , [198,69,36] , [142,37,29] , [255,80,0] , [237,118,20] , [255,162,20] , [255,200,37]]
# colorsRow3 = [[255,235,87] , [211,252,126] , [153,230,95] , [90,197,79] , [51,152,75] , [30,111,80] , [19,76,76] , [12,46,68] , [0,57,109] , [0,105,170] , [0,152,220] , [0,205,249] , [12,241,255] , [148,253,255] , [253,210,237] , [243,137,245]]
# colorsRow4 = [[219,63,253] , [122,9,250] , [48,3,217] , [12,2,147] , [3,25,63] , [59,20,67] , [98,36,97] , [147,56,143] , [202,82,201] , [200,80,134] , [246,129,135] , [245,85,93] , [234,50,60] , [196,36,48] , [137,30,43] , [87,28,39]]

# may have to rewrite this using ai bc some color choices are off if not b/w
def closestColor(rgbCode):
    colors = np.array(allColors)
    color = np.array(rgbCode)
    distances = np.sqrt(np.sum((colors-color)**2,axis=1))

    # returns the actual color
    # index_of_smallest = np.where(distances == np.amin(distances))
    # smallest_distance = colors[index_of_smallest]
    # return smallest_distance

    # returns array loc
    result = np.where(distances == np.amin(distances))
    return result[0][0]

def getIndexInGUI(where):
    if where <= 15:
        return "" + str(where+1) + "," + str(1)
    elif where <= 31:
        return "" + str(where-15) + "," + str(2)
    elif where <= 47:
        return "" + str(where-31) + "," + str(3)
    else:
        return "" + str(where-47) + "," + str(4)

def closestGui(code):
    return getIndexInGUI( closestColor(code) )


def colorSelector(code):
    colorLoc = closestGui(code)
    temp = colorLoc.split(',')
    x = int(temp[0]) * 121 + 58 - 121
    y = int(temp[1]) * 25 + 955 - 25
    pg.moveTo(x, y, duration=.5)
    pg.mouseDown()
    pg.mouseUp()

# returns an array called data with the color of every pixel in the image
img = cv2.imread('shapeTest.jpg')
heightImg, widthImg, _ = np.shape(img)
data = np.reshape(img, (heightImg * widthImg, 3))
data = np.float32(data)


# implement some way to ask user to hover over top left corner take x,y then go to bot right
def defaultBg(topLeftX,topLeftY,botRightX,botRightY,colorLoc):
    temp = colorLoc.split(',')
    x = int(temp[0]) * 121 + 58 - 121
    y = int(temp[1]) * 25 + 955 - 25
    pg.moveTo(x,y,duration=.5)
    pg.mouseDown()
    pg.mouseUp()
    # go from left to right while mouse down (on cooldown)
    # go down 6 pixels
    for y in range( math.ceil((botRightY-topLeftY) / 6) ):
        if keyboard.is_pressed("b"):
            break
        pg.moveTo(topLeftX, topLeftY + y * 6, duration=0.5)
        pg.mouseDown()
        pg.moveRel(botRightX-topLeftX+3, 0, duration=0.8)
        pg.mouseUp()

def askForColor():
    ints = []
    ints.append(int(input("first hex? ")))
    ints.append(int(input("second hex? ")))
    ints.append(int(input("third hex? ")))
    return ints

# returns x, y
def getPoint(index):
    return   (index % width) , (index // width)
# returns index for numpy array
def getIndex(y,x):
    return x*width + y

# fix to work with indexes instead of points using getIndex
def getEuDist(index1, index2):
    x1 = getPoint(index1)[0]
    y1 = getPoint(index1)[1]
    x2 = getPoint(index2)[0]
    y2 = getPoint(index2)[1]
    return math.sqrt( (x1 - x2)**2 + (y1-y2)**2 )

prevIndex = -1
# use to color any given index the correct color (individually)
# working but test with a basic image
def colorPoint(index):
    global prevIndex
    if closestColor(data[index]) != prevIndex:
        colorSelector(data[index])
        prevIndex = closestColor(data[index])
    x, y = getPoint(index)
    x = x + topLeftX
    y = y + topLeftY
    pg.moveTo(x, y, duration=.2)
    pg.mouseDown()
    return prevIndex

# fix
# works but will brick the ui if its a complicated sketch
def multiColor(first, last, rowsSkipped, pixelsSkipped):
    for x in range(first, last, (rowsSkipped * width)):
        pg.mouseUp()
        for z in range(0,width,pixelsSkipped):
            if z == (width-2) or z == 0:
                colorPoint(z + x)
                if z == (width-2):
                    pg.mouseUp()
            elif closestColor(data[z+x+pixelsSkipped]) == prevIndex:
                count = 0
            else:
                colorPoint(z + x)
                pg.mouseDown()
                if closestColor(data[z + x + pixelsSkipped]) != prevIndex:
                   pg.mouseUp()

def collectIndices(hexIndex):
    loc = []
    for x in range(0, 40400):
        if closestColor(data[x]) == hexIndex:
            loc.append(getPoint(x))
    return loc

def blackDot(x,y):
    pg.moveTo(x, y, duration=.2)
    pg.mouseDown()
    pg.mouseUp()


# multiColor(8000,40400,6,12)
# pg.mouseUp()

# next section of code is to draw any given singular shape
# by passing in an image with one shape and the necessary color, I have to make it be able to draw that shape correctly (eventually efficiently)
def draw_shape(shape, color):
    colorSelector(color)


n = 255,255,0
# passing in param such as color, and then an list of all x, y or an image and being able to process that image
draw_shape(img, n)
pg.mouseUp()
