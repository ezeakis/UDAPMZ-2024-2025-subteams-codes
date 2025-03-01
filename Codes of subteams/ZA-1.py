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
l = (0, 255, 127)
h = (0, 255, 255)
a = (255, 255, 255)
c = (0, 0, 0)
t = (255, 186, 0)
for i in range(28):
    rgb = sense.color
    c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour
    
    image = [     
        h, h, h, h, h, h, h, h,
        h, t, t, h, h, h, h, h,
        h, t, t, h, h, h, h, h,
        t, t, t, h, h, h, h, h,
        t, c, t, t, t, t, t, h,
        t, t, t, t, t, t, t, a,
        h, h, h, t, h, h, t, h,
        l, l, l, l, l, l, l, l
    ]
    
    sense.set_pixels(image)
    sleep(.5)                
    
    rgb = sense.color
    c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour
    image = [
        h, t, t, h, h, h, h, h,
        h, t, t, h, h, h, h, h,
        t, t, t, h, h, h, h, h,
        t, c, t, t, t, t, t, h,
        t, t, t, t, t, t, t, a,
        h, h, h, t, h, h, t, h,
        h, h, h, h, h, h, h, h,
        l, l, l, l, l, l, l, l
    ]
    sense.set_pixels(image)
    sleep(.5)                                 


x = (165, 130, 234)
sense.clear(x)





# Display the image
