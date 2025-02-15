from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
orange = (255,136,0)

def flower():
    B = blue 
    R = red
    O = orange
    G = green
    logo = [
    B, B, B, R, R, B, B, B, 
    B, B, R, O, O, R, B, B,
    B, B, R, O, O, R, B, B,
    B, B, B, R, R, B, B, B,
    G, G, B, G, G, B, G, G,
    B, G, G, G, G, G, G, B,
    B, B, G, G, G, G, B, B,
    B, B, B, G, G, B, B, B,
    ]
    return logo

def butterfly():
    G = green
    R = red
    B = blue 
    O = nothing
    W = white
    Y = yellow
    logo = [
    B, O, B, B, B, B, O, B,
    B, B, W, B, B, W, B, B,
    B, B, B, W, W, B, B, B, 
    B, Y, Y, W, W, Y, Y, B,
    Y, G, Y, W, W, Y, G, Y,
    Y, G, Y, W, W, Y, G, Y,
    B, Y, Y, W, W, Y, Y, B,
    B, B, B, Y, Y, B, B, B,
    ]
    return logo

def earth():
    O = nothing
    B = blue
    W = white
    Y = yellow
    G = green
    R = red
    logo = [
    Y, O, O, O, O, O, O, O, 
    O, O, R, O, O, O, O, O, 
    O, O, W, O, O, O, O, O, 
    Y, O, Y, O, O, O, Y, O, 
    O, O, O, O, O, O, O, Y, 
    O, B, B, B, B, B, B, O, 
    B, B, G, B, B, G, G, B, 
    G, B, B, B, G, B, G, B, 
    ]
    return logo

def roket():
    Y = yellow
    R = red
    O = nothing
    B = blue
    W = white
    logo = [
    O, O, O, R, R, O, O, O, 
    O, O, R, R, R, R, O, O,
    O, O, W, W, W, W, O, O, 
    O, O, W, B, B, W, O, O,
    O, O, W, B, B, W, O, O,
    O, R, W, W, W, W, R, O,
    O, R, W, W, W, W, R, O,
    O, R, O, Y, Y, O, R, O,
    ]
    return logo

def alien():
    W = white
    O = nothing
    logo = [
    O, O, W, W, W, W, O, O,
    O, W, W, W, W, W, W, O,
    W, O, O, W, W, O, O, W,
    W, O, O, W, W, O, O, W,
    W, W, W, W, W, W, W, W,
    O, W, O, W, W, O, W, O,
    O, O, W, O, O, W, O, O,
    O, O, O, W, W, O, O, O,
    ]
    return logo

images = [flower, butterfly, earth, roket, alien, ]
count = 0

while True:  
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1
