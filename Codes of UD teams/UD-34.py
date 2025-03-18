from sense_hat import SenseHat
import time
s = SenseHat()
s.low_light = True

brown1 = (90,20,0)
brown2 = (72,34,0)
brown3 = (90,5,0)
pink = (165,15,90)
red = (255,0,0)
orange1= (165,45,0)
orange2 = (140,55,0)
yellow = (55,55,0)
green1 = (0,75,0)
green2 = (0,100,0)
green3 = (0,79,0)
cyan = (0,85,85)
blue = (0,0,255)
purple = (78,0,195)
black = (0,0,0)
white = (255,255,255)

B1 = brown1
B2 = brown2
B3 = blue
B4 = black
B5 = brown3
G1 = green1
G2 = green2
G3 = green3
P1 = pink
P2 = purple
R = red
O1 = orange1
O2 = orange2
Y = yellow
C = cyan
W = white

#日本に生えている木。
#A tree growing in Japan.

def tree():
    logo = [
    W, W, G3, G3, G3, G3, W, W,
    W, G3, G3, G3, G3, G3, G3, W,
    W, G3, G3, G3, G3, G3, G3, W,
    W, G3, G3, G3, G3, G3, G3, W,
    W, G3, G3, G3, G3, G3, G3, W,
    W, W, W, B1, B1, W, W, W,
    W, W, W, B1, B1, W, W, W,
    W, W, W, B1, B1, W, W, W,
    ]
    return logo
  
#日本に咲いているチューリップ。
#Tulips blooming in Japan.

def tulip():
    logo = [
    W, W, W, W, W, W, W, W,
    W, P1, W, P1, W, P1, W, W,
    W, P1, P1, P1, P1, P1, W, W,
    W, P1, P1, P1, P1, P1, W, W,
    W, W, P1, P1, P1, W, W, W,
    W, W, W, G2, W, W, W, W, 
    W, G2, W, G2, W, G2, W, W,
    W, W, G2, G2, G2, W, W, W,
    ]
    return logo
    
#犬。
#dog.

def dog():
    
    logo = [
    W, W, W, W, W, W, W, W,
    B1, B2, B2, B2, B2, B1, B1, W,
    B1, B4, B2, B4, B2, B1, B1, W,
    B1, B2, B2, B2, B2, B1, B1, W,
    B1, B4, B4, B4, B2, B1, B1, W,
    W, B2, B2, B2, B2, W, W, W,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    ]
    return logo
    
#虹。
#rainbow.

def rainbow():
    
    logo = [
    W, R, R, R, R, R, R, R,
    R, R, O1, O1, O1, O1, O1, O1,
    R, O1, O1, Y, Y, Y, Y, Y,
    R, O1, Y, Y, G1, G1, G1, G1,
    R, O1, Y, G1, G1, C, C, C,
    R, O1, Y, G1, C, C, B3, B3, 
    R, O1, Y, G1, C, B3, B3, P2,
    R, O1, Y, G1, C, B3, P2, W,
    ]
    return logo
    
#キツネ。
#fox.

def fox():
    
    logo = [
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, O2, W, W,
    W, W, W, W, O2, O2, B4, W,
    B4, B5, W, O2, O2, O2, O2, B4,
    B5, W, O2, O2, O2, O2, W, W,
    W, O2, O2, O2, O2, O2, W, W,
    W, O2, O2, W, W, O2, W, W,
    W, W, W, W, W, W, W, W,
    ]
    return logo
    
#パンダ。
#panda.

def panda():
    
    logo = [
    B4, B4, W, W, B4, B4, W, W,
    B4, B4, W, W, B4, B4, W, W,
    W, W, W, W, W, W, B4, B4,
    W, B4, W, W, B4, W, B4, B4,
    W, B4, W, W, B4, W, B4, B4,
    W, W, B4, B4, W, W, B4, B4,
    W, W, W, W, W, B4, B4, W,
    W, B4, B4, B4, B4, B4, W, W,
    ]
    return logo
    
#カメ。
#turtle.

def turtle():
    
    logo = [
    W, W, B4, Y, B4, W, W, W,
    W, W, Y, Y, Y, W, W, W,
    Y, G3, G3, G3, G3, G3, Y, W,
    W, G3, G3, G3, G3, G3, W, W,
    W, G3, G3, G3, G3, G3, W, W,
    W, G3, G3, G3, G3, G3, W, W,
    W, Y, W, Y, W, Y, W, W,
    W, W, W, Y, W, W, W, W,
    ]
    return logo
    
def image1():
    G = (124, 130, 138)
    g = (177, 184, 180)                 
    B = (47, 69, 153)
    b = (153, 217, 214)
    w = (255, 255, 255)
    p = (255, 177, 36)
    l = (0, 0, 0)
    y = (245, 156, 36)

    rgb = s.color # get the colour from the sensor
    b = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      y, b, G, G, G, b, b, b,
      b, G, g, g, g, G, w, w,
      w, G, l, g, l, G, b, b,
      b, G, p, G, p, G, b, b,
      B, B, B, G, G, G, B, B,
      B, G, g, g, g, G, g, G,
      B, G, g, g, g, g, G, B,
      B, B, G, G, G, G, B, B ]
    return image

def image2():
    R = (237, 28, 36)
    G = (34, 177, 76)
    B = (0, 183, 239)
    D = (47, 54, 153)
    g = (177, 184, 180)                 

    rgb = s.color # get the colour from the sensor
    D = (rgb.red, rgb.green, rgb.blue)
    
    
    image = [
       g, D, D, D, D, D, D, D,
       D, D, G, G, G, D, D, D,
       D, D, G, G, G, D, D, D,
       R, R, R, R, R, R, R, R,
       R, B, R, R, R, R, B, R,
       R, R, R, R, R, R, R, R,
       R, R, R, B, B, R, R, R,
       G, G, G, G, G, G, G, G]
    return image
    
images = [tree, tulip, dog, rainbow, fox, panda, turtle, image1, image2]
count = 0

for i in range(len(images)): 
    s.set_pixels(images[count % len(images)]())
    time.sleep(2)
    count += 1
