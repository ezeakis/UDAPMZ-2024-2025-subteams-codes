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
b = (105, 105, 105) # DimGray
c = (0, 0, 0) # Black
d = (100, 149, 237) # CornflowerBlue
v = (255, 0, 0) # Red
z = (153, 50, 204) # DarkOrchid

for i in range(28):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour
                           
    image = [
        c, c, v, c, v, c, c, c,
        c, z, z, z, z, v, c, c,
        z, b, z, b, z, c, c, c,
        z, z, z, z, z, v, c, c,
        c, c, d, d, d, c, c, z,
        c, z, d, z, z, z, z, c,
        c, c, d, d, z, c, c, c,
        c, c, z, c, z, c, c, c]                        
    # Display the image
    sense.set_pixels(image)
    sleep(1)

x = (178, 34, 34)  # choose your own red, green, blue values between 0 - 255
sense.clear(x)