# Import the libraries
from sense_hat import SenseHat
from time import sleep

# Set up the Sense HAT
sense = SenseHat()
sense.set_rotation(270, False)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken

for i in range(14):
   
    #GR-21
    a = (255, 255, 255) # White
    c = (0, 0, 0) # Black
    f = (25, 25, 112) # MidnightBlue
    m = (34, 139, 34) # ForestGreen
    r = (225, 0, 0) # red

    rgb = sense.color # λήψη του χρώματος από τον αισθητήρα
    c = (rgb.red, rgb.green, rgb.blue)

image = [
  r, a, a, c, c, a, a, r,
  a, c, c, a, a, c, c, a,
  a, c, r, a, a, r, c, a,
  c, a, a, r, r, a, a, c,
  c, a, a, r, r, a, a, c,
  a, c, r, a, a, r, c, a,
  a, c, c, a, a, c, c, a,
  r, a, a, c, c, a, a, r]

    # Display the image

sense.set_pixels(image)
sleep(1)

    #ZA-11
a = (255, 255, 255) # White
b = (105, 105, 105) # DimGray
c = (0, 0, 0) # Black
d = (100, 149, 237) # CornflowerBlue
s = (139, 69, 19) # SaddleBrown
t = (255, 140, 0) # DarkOrange
e = (0, 0, 205) # MediumBlue
g = (0, 191, 255) # DeepSkyBlue
q = (255, 255, 0) # Yellow
v = (255, 0, 0) # Red
m = (34, 139, 34) # ForestGreen

rgb = sense.color # get the colour from the sensor
c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour
 
  #moon 
image1 = [
    c, c, c, c, c, c, c, c,
    c, a, c, c, c, c, c, c, 
    c, c, c, b, b, c, c, c,
    c, c, b, b, c, c, c, c, 
    c, c, b, b, c, c, c, c, 
    c, c, c, b, b, c, a, c, 
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, c, c]

  #black heart
image2 = [
    a, a, a, a, a, a, a, a,
    a, c, c, a, a, c, c, a,
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, c, c,
    a, c, c, c, c, c, c, a,
    a, a, c, c, c, c, a, a,
    a, a, a, c, c, a, a, a,
    a, a, a, a, a, a, a, a]
 
  #cross
image3 = [
    a, a, a, s, s, a, a, a,
    a, a, a, s, s, a, a, a,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    a, a, a, s, s, a, a, a,
    a, a, a, s, s, a, a, a,
    a, a, a, s, s, a, a, a,
    a, a, a, s, s, a, a, a]
 
  #sun
image4 = [
    g, g, g, g, t, q, q, q,
    g, g, g, g, t, q, q, q,
    g, m, m, g, g, t, q, q,
    m, m, m, m, g, g, t, t,
    m, s, s, m, g, g, g, g,
    g, s, s, g, g, g, g, g,
    g, s, s, g, g, g, g, g,
    m, m, m, m, m, m, m, m]
 
  #red heart
image5 = [
    a, a, a, a, a, a, a, a,
    a, v, v, a, a, v, v, a,
    v, v, v, v, v, v, v, v,
    v, v, v, v, v, v, v, v,
    a, v, v, v, v, v, v, a,
    a, a, v, v, v, v, a, a,
    a, a, a, v, v, a, a, a,
    a, a, a, a, a, a, a, a]

# Display the image
for i in range(6):
    
    sense.set_pixels(image1)
    sleep(2)
    sense.set_pixels(image2)
    sleep(2)
    sense.set_pixels(image3)
    sleep(2)
    sense.set_pixels(image4)
    sleep(2)
    sense.set_pixels(image5)
    sleep(2)


x = (111, 3, 54)  
sense.clear(x)
