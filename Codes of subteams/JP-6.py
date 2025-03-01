from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
brown=(233,113,50)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
light_green=(144,238,144)

def tree_logo():
    G = green
    Y = yellow
    B = brown
    O = nothing
    logo = [
    O, O, G, G, G, G, O, O,
    O, G, G, G, G, G, G, O,
    O, G, G, G, G, G, G, O,
    O, O, G, G, G, G, O, O,
    O, O, O, B, B, O, O, O,
    O, B, O, B, B, B, O, O,
    O, O, B, B, B, O, O, O,
    O, O, O, B, B, O, O, O,
    ]
    return logo

def mountain_logo():
    G = green
    L = light_green
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O,
    O, O, G, O, O, O, O, L, 
    O, G, G, G, O, O, L, L,
    G, G, G, G, G, L, L, L,
    G, G, G, G, G, G, L, L,
    G, G, G, G, G, G, G, L,
    G, G, G, G, G, G, L, G,
    ]
    return logo

def beetle_logo():
    B = brown
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    O, B, O, O, B, B, O, O,
    B, B, O, O, O, O, B, O, 
    O, O, B, O, B, O, B, O,
    O, O, O, B, B, O, B, O,
    B, O, B, B, B, B, B, B,
    B, O, O, O, B, B, B, B,
    O, B, B, B, B, B, B, B,
    ]
    return logo

#石本逞 / Ishimoto Takuma
blue1 = (0, 0, 255)
blue2 = (17, 85, 204)
nothing = (255, 255, 255)
 
def whale():
    B1 = blue1
    B2 = blue2
    N = nothing
    logo = [
    N, B2, B2, B2, N, N, N, N,
    B2, N, B2, N, B2, N, N, N,
    N, N, B2, N, N, N, N, N,
    N, N, B2, N, N, N, N, N,
    N, B1, B1, B1, N, N, N, N,
    B1, B1, B1, B1, B1, N, N, B1,
    B1, B1, B1, B1, B1, N, B1, B1,
    B1, B1, B1, B1, B1, B1, B1, B1,
    ]
    return logo

images = [tree_logo, mountain_logo, beetle_logo, whale]
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(1.5)
    count += 1