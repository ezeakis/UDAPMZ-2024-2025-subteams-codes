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
orenge=(225,125,0)
lightblue=(52, 235, 198)

def egg():
    G = green
    Y = yellow
    B = blue
    O = nothing
    K = orenge
    W = white
    logo = [
    B, B, B, K, W, B, B, B,
    B, B, W, W, W, K, B, B,
    B, W, W, K, W, W, W, B,
    B, W, W, W, W, W, K, B,
    B, K, W, W, K, W, W, B,
    B, W, W, W, W, W, W, B,
    B, B, W, K, W, K, B, B,
    G, G, G, G, G, G, G, G,   ]
    return logo

def yama():
    G = green
    R = red
    O = nothing
    W = white 
    B = blue
    L = lightblue
    logo = [
    B, B, B, B, B, B, B, B, 
    B, B, B, W, W, B, B, B,
    B, B, W, W, W, W, B, B, 
    B, W, W, W, W, W, W, W,
    W, W, W, L, W, W, W, W,
    L, W, L, L, L, L, L, W,
    L, L, L, L, L, L, L, L,
    L, L, L, L, L, L, L, L,
    ]
    return logo

def natu():
    G = green
    Y = yellow
    B = blue
    O = nothing
    K = orenge
    W = white
    logo = [
    B, B, B, B, B, B, Y, Y,
    B, W, W, B, B, B, Y, Y,
    W, B, W, B, B, B, B, B,
    B, W, K, K, K, K, K, K,
    B, W, K, K, K, K, K, B,
    B, W, K, K, K, K, B, B,
    B, B, W, K, K, B, B, B,
    G, G, G, G, G, G, G, G,   ]
    return logo

def huyu():
    G = green
    Y = yellow
    B = blue
    O = nothing
    K = orenge
    W = white
    logo = [
    B, B, B, B, B, B, W, B,
    B, W, W, B, W, B, B, B,
    W, B, W, B, B, B, B, B,
    B, W, W, W, W, W, W, W,
    B, W, W, W, W, W, W, B,
    B, W, W, W, W, W, B, B,
    B, B, W, W, W, B, B, B,
    W, W, W, W, W, W, W, W,   ]
    return logo


images = [egg, yama , natu, huyu,]
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1