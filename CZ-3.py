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

# Blanka Feixová
for i in range(6):
    rgb = sense.color # get the colour from the sensor

    z = (rgb.red, rgb.green, rgb.blue)
    image = [
        b, b, z, z, z, z, b, b,
        w, b, b, b, b,b, b, w,
        b, b, b, b, b, b, b, b,
        b, a, c, b, b, c, a, b,
        b, b, b, b, b, b, b, b,
        b, b, b, a, a, b, b, b,
        b, b, a, v, v, a, b, b,
        b, b, a, a, a, a, b, b]

    # Display the image
    sense.set_pixels(image)
    sleep(1)

sense.clear()
z = (153, 50, 204) # DarkOrchid

# Jakub Brabec
for i in range(6):
    rgb = sense.color # get the colour from the sensor

    a = (rgb.red, rgb.green, rgb.blue)
    image = [
      a, a, a, v, a, v, a, a,
      a, a, a, v, v, v, a, a,
      a, a, a, v, v, v, a, a,
      a, a, a, a, v, a, a, a,
      a, a, a, a, m, a, a, a,
      a, a, s, s, s, s, s, a,
      a, a, a, s, s, s, a, a,
      a, a, a, s, s, s, a, a,
    ]

    # Display the image
    sense.set_pixels(image)
    sleep(1)

sense.clear()
a = (255, 255, 255) # White

