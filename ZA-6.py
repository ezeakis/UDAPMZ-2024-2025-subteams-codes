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

# Display the image

g = (250, 216, 22) # GoldBell
b = (173, 113, 2) # KittyCatBrown
r = (189, 50, 19) # CollarRed
e = (9, 7, 120) # BlackBlueKittyEyes
s = (0, 0, 0) # BlackStage

for i in range(14):
    rgb = sense.color # get the colour from the sensor
    s = (rgb.red, rgb.green, rgb.blue) # use the sensed colour
   
    image = [
      s, s, s, s, s, s, s, s,
      s, s, s, s, s, s, s, s,
      s, s, s, b, s, s, b, s,
      s, s, s, b, b, b, b, s,
      s, s, s, e, b, e, b, s,
      s, b, s, b, b, b, b, s,
      s, b, s, r, r, r, r, s,
      s, s, b, b, g, b, b, s]
   
    # Display the image
    sense.set_pixels(image)
    sleep(1)
    image = [
      s, s, s, s, s, s, s, s,
      s, s, s, b, s, s, b, s,
      s, s, s, b, b, b, b, s,
      s, s, s, e, b, e, b, s,
      s, b, s, b, b, b, b, s,
      s, b, s, r, r, r, r, s,
      s, s, b, b, g, b, b, s,
      s, s, s, s, s, s, s, s]
   
    # Display the image
    sense.set_pixels(image)
    sleep(1)