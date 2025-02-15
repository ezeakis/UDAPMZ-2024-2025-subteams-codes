# Import the libraries
from sense_hat import SenseHat
from time import sleep

# Set up the Sense HAT
sense = SenseHat()
sense.set_rotation(270, False)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken

# Colour palette
a = (255, 255, 255) # White
b = (105, 105, 105) # DimGray
c = (0, 0, 0) # Black
d = (100, 149, 237) # CornflowerBlue
e = (0, 0, 205) # MediumBlue
f = (25, 25, 112) # MidnightBlue
g = (0, 191, 255) # DeepSkyBlue
h = (0, 255, 255) # Cyan
j = (143, 188, 143) # DarkSeaGreen
k = (46, 139, 87) # SeaGreen
l = (0, 255, 127) # SpringGreen
m = (34, 139, 34) # ForestGreen
n = (154, 205, 50) # YellowGreen
o = (128, 128, 0) # Olive
p = (240, 230, 140) # Khaki
q = (255, 255, 0) # Yellow
r = (184, 134, 11) # DarkGoldenrod
s = (139, 69, 19) # SaddleBrown
t = (255, 140, 0) # DarkOrange
u = (178, 34, 34) # Firebrick
v = (255, 0, 0) # Red
w = (255, 192, 203) # Pink
y = (255, 20, 147) # DeepPink
z = (153, 50, 204) # DarkOrchid

# Stella Bohatá
for i in range(6):
    rgb = sense.color # get the colour from the sensor

    s = (rgb.red, rgb.green, rgb.blue) # use the sensed colour
    image = [
      r, r, r, r, r, r, r, r,
      r, s, e, e, e, e, s, r,
      s, e, a, a, a, a, e, s,
      s, h, a, h, h, a, h, s,
      s, y, a, y, y ,a ,y ,s,
      s, c, a, a, a, a, c, s,
      s, y, e, e, e, e, y, s,
      s, h, h, h, h, h, h, s]

    # Display the image
    sense.set_pixels(image)
    sleep(1)

sense.clear()
s = (139, 69, 19) # SaddleBrown

# Štěpán Bohatý
for i in range(6):
    rgb = sense.color # get the colour from the sensor

    y = (rgb.red, rgb.green, rgb.blue)
    image = [
      y, y, y, y, y, y, y, y,
      y, c, c, c, c, c, c, y,
      y, c, c, a, a, c, c, y,
      y, c, a, c, c, a, c, y,
      y, c, a, a, a ,a ,c ,y,
      y, c, c, c, c, c, c, y,
      y, c, c, c, c, c, c, y,
      y, c, c, c, c, c, c, y]

    # Display the image
    sense.set_pixels(image)
    sleep(1)

sense.clear()
y = (255, 20, 147) # DeepPink

