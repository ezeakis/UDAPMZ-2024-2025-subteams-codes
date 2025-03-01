# Import the libraries
from sense_hat import SenseHat
from time import sleep

# Set up the Sense HAT
sense = SenseHat()
sense.set_rotation(270, False)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken

# Add colour variables and image
c = (255, 220, 8) #cream
b = (0, 0, 0) #black
r = (223, 158, 20) #brown
o = (3,150,255) #blue


for i in range(28):
    rgb = sense.color # get the colour from the sensor
    o = (rgb.red, rgb.green, rgb.blue)
    # Display the image
    image = [
    b, b, o, o, o, o, b, b,
    b, b, c, b, b, c, b, b,
    c, b, b, c, c, b, b, c,
    c, b, b, c, c, b, b, c,
    c, c, c, r, r, c, c, c,
    o, c, b, b, b, b, c, o,
    o, c, b, b, b, b, c, o,
    o, c, c, c, c, c, c, o]
    
    sense.set_pixels(image)
    sleep(1)