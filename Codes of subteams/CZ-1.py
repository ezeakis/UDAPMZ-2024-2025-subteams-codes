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

#Emilia Teterja
c = (171, 228, 250) # Černá
b = (105, 105, 105) # Tmavě šedá
a = (255, 255, 255) # Bílá
d = (0,0,0)
e = (255, 255, 7)
f = (2, 126, 7)
g = (2, 82, 253)

for i in range(6):
    rgb = sense.color # get the colour from the sensor

    a = (rgb.red, rgb.green, rgb.blue)
    image = [
        c, c, c, c, c, c, e, e,
        c, b, b, b, c, c, e, e,
        c, b, c, b, c, c, b, b,
        c, b, c, g, c, b, b, b,
        c, b, b, c, c, b, d, b,
        c, b, b, b, b, b, b, b,
        c, c, b, b, a, b, b, b,
        f, f, f, f, a, b, b, b]


    # Display the image
    sense.set_pixels(image)
    sleep(1)

sense.clear()
a = (255, 255, 255) # White
b = (105, 105, 105) # DimGray
c = (0, 0, 0) # Black
d = (100, 149, 237) # CornflowerBlue
e = (0, 0, 205) # MediumBlue
f = (25, 25, 112) # MidnightBlue
g = (0, 191, 255) # DeepSkyBlue


# Anežka Makovičková
z = (253, 255, 0) # žlutá
o = (244, 142, 25) # oranžová
s = (255, 0, 0) # světlečervená
c = (200, 0, 0) # červená
t = (0, 183, 0) # Tmavě zelená
e = (0, 234, 0) # světlezelená
h = (162, 111, 84) # hnědá
for i in range(6):
    rgb = sense.color # get the colour from the sensor

    t = (rgb.red, rgb.green, rgb.blue)
    image = [
      t, e, t, h, t, e, t, e,
      e, t, e, h, e, t, e, t,
      t, e, c, c, c, e, t, e,
      e, c, s, o, z, c, e, t,
      t, c, s, o, o, c, t, e,
      e, c, s, s, s, c, e, t,
      t, e, c, c, c, e, t, e,
      e, t, e, h, e, t, e, t]

    # Display the image
    sense.set_pixels(image)
    sleep(1)

sense.clear()
z = (153, 50, 204) # DarkOrchid
o = (128, 128, 0) # Olive
s = (136, 0, 27) # red
c = (0, 0, 0) # Black
t = (255, 140, 0) # DarkOrange
e = (47, 46, 46) # grey
h = (65, 64, 64) # grey
