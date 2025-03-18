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

  #GR-22
  n = (154, 205, 50) # YellowGreen
  c = (0, 0, 0) # Black

  rgb = sense.color # get the colour from the sensor
  c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

  image = [
  n,n,n,n,n,n,n,n,
  n,n,n,n,n,n,n,n,
  n,c,c,n,n,c,c,n,
  n,c,c,n,n,c,c,n,
  n,n,n,n,n,n,n,n,
  n,c,n,n,n,n,c,n,
  n,n,c,c,c,c,n,n,
  n,n,c,c,c,c,n,n]

  # Display the image
  sense.set_pixels(image)
  sleep(1)

  #ΖΑ-3

  c = (0, 0, 0) # Black
  a = (255, 255, 255) # white
  t = (255, 140, 0) # dark orange

  rgb = sense.color # get the colour from the sensor    
  c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour
          
  image = [
      t, a, t, c, c, t, a, t,
      t, a, t, c, c, t, a, t,
      t, t, t, t, t, t, t, t,
      t, a, c, t, t, c, a, t,
      t, t, t, t, t, t, t, t,
      a, a, a, c, c, a, a, a,
      c, a, a, a, a, a, a, c,
      c, c, a, a, a, a, c, c]
      # Display the image
  sense.set_pixels(image)
  sleep(1)

  x = (92, 4, 3)  
  sense.clear(x)
