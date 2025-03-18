from sense_hat import SenseHat
import time

sense = SenseHat()
sense.low_light = True

s = (139, 69, 19) # ΚαφέΣέλας
c = (0, 0, 0) # Black
t = (255, 140, 0) # DarkOrange

black = (0,0,0)
#outer space and insect wings
orange = (255,136,0)
#leaves
gray = (89,89,89)
#sky
yellow = (255,247,0)
#the insect and rainbow
green = (44,163,0)
#ground(grass)
red = (219,0,0)
#the bird and rainbow
brown = (133,77,0)
#dirt
dark_brown = (66,39,0)
#wood
white = (255,255,255)
#galaxy
light_yellow = (251,255,30)
#star
lime = (4,255,0)
#rainbow
blue = (0,129,184)
#earth in galaxy

def sapling():
  o = orange
  d = dark_brown
  G = green
  b = brown
  g = gray
  logo = [
      g,g,g,g,g,g,g,g,
      g,g,g,g,g,g,g,g,
      g,g,g,g,g,g,g,g,
      g,g,g,g,g,g,g,g,
      g,g,o,g,o,g,g,g,
      g,g,g,d,g,g,g,g,
      G,G,G,G,G,G,G,G,
      b,b,b,b,b,b,b,b,
  ]
  return logo

def tree():
  o = orange
  d = dark_brown
  g = gray
  G = green
  b = brown
  logo = [
    g,g,g,o,o,g,g,g,
    g,g,o,o,o,o,o,g,
    g,g,o,o,o,o,o,g,
    g,g,o,d,o,o,g,g,
    g,g,g,d,d,g,g,g,
    g,g,g,d,d,g,g,g,
    G,G,G,G,G,G,G,G,
    b,b,b,b,b,b,b,b,
  ]
  return logo
  
def bear_fruits():
  o = orange
  d = dark_brown
  g = gray
  G = green
  b = brown
  r = red
  logo = [
    g,g,g,o,o,g,g,g,
    g,g,o,r,o,o,o,g,
    o,g,o,o,o,r,o,g,
    r,d,r,d,o,o,g,g,
    o,o,d,d,d,d,o,g,
    g,g,g,d,d,g,g,g,
    G,G,G,G,G,G,G,G,
    b,b,b,b,b,b,b,b,
  ]
  return logo
    
def insect():
  g = gray
  d = dark_brown
  y = yellow
  b = black
  logo = [
    g,g,d,d,d,d,g,g,
    g,g,d,d,d,d,g,d,
    g,g,d,d,d,d,d,d,
    g,d,d,b,y,b,d,d,
    d,d,b,y,y,y,b,g,
    d,d,b,b,b,b,b,g,
    g,g,d,b,y,b,g,g,
    g,g,d,d,d,d,g,g,
  ]
  return logo
  
def bird():
  g = gray
  r = red
  y = yellow
  b = black
  logo =[
    b,b,b,b,g,g,g,g,
    g,g,g,g,r,r,g,g,
    b,r,r,g,r,b,r,y,
    g,r,r,r,r,r,g,b,
    b,b,r,r,r,r,g,g,
    g,g,r,r,r,g,g,g,
    b,b,r,r,g,g,g,g,
    g,g,g,g,g,g,g,g,
  ]
  return logo
  
def rainbow():
  r = red
  o = orange
  y = yellow
  l = lime
  d = dark_brown
  g = gray
  G = green
  b = brown
  logo =[
    g,g,g,r,r,r,g,g,
    g,r,r,o,y,y,r,r,
    r,y,o,o,o,l,y,y,
    y,l,o,o,o,g,l,l,
    l,g,g,d,g,g,r,g,
    g,g,g,d,g,g,r,r,
    G,G,G,G,G,G,G,G,
    b,b,b,b,b,b,b,b,
  ]
  return logo
  
def planet():
  b = black
  w = white
  g = gray
  G = green
  logo =[
    b,b,b,b,b,b,b,b,
    b,b,b,b,w,b,b,b,
    b,w,b,g,g,b,w,b,
    b,b,g,G,G,g,b,b,
    b,g,G,G,G,g,g,b,
    b,g,g,g,g,G,g,b,
    b,b,g,G,G,g,w,b,
    b,b,b,g,g,b,b,b,
  ]
  return logo
  
def galaxy():
  b = black
  y = light_yellow
  g = gray
  w = white
  B = blue
  logo = [
    b,y,b,b,b,b,b,b,
    b,b,b,b,b,w,w,b,
    y,b,b,b,w,w,w,b,
    b,b,y,w,y,w,b,b,
    y,b,w,y,y,w,b,b,
    b,w,w,y,w,b,b,b,
    b,w,B,g,b,b,y,b,
    b,b,b,b,b,b,w,b,
  ]
  return logo

def image():
  rgb = sense.color # get the colour from the sensor
  t = (rgb.red, rgb.green, rgb.blue)
  logo = [
    t,t,t,t,t,t,t,t,
    t,s,s,s,s,s,s,t,
    t,s,s,s,s,s,s,t,
    t,s,s,c,s,c,s,t,
    t,s,s,s,c,s,s,t,
    t,s,s,s,s,s,s,t,
    t,s,s,s,s,s,s,t,
    t,t,t,t,t,t,t,t,
  ]
  return logo 

images = [sapling, tree, bear_fruits, insect, bird, rainbow, planet, galaxy, image]
count = 0

for i in range(len(images)): 
    sense.set_pixels(images[count % len(images)]())
    time.sleep(1)
    count += 1
