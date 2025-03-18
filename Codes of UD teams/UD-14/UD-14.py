# UD-14
# Fox Code
# Εισαγωγή βιβλιοθηκών

# Import the libraries
from sense_hat import SenseHat
from time import sleep

# Set up the Sense HAT
sense = SenseHat()
sense.set_rotation(270, False)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken
# Ρύθμιση του αισθητήρα χρωμάτων
sense.color.gain = 60 # Ρύθμιση της ευαισθησίας του αισθητήρα
sense.color.integration_cycles = 64 # Το μεσοδιάστημα κατά το οποίο θα γίνεται η ανάγνω

# Add colour variables and image
c = (0, 0, 0) # Black
a = (255, 255, 255) # white
t = (255, 140, 0) # dark orange
image1 = [
t, a, t, c, c, t, a, t,
t, a, t, c, c, t, a, t,
t, t, t, t, t, t, t, t,
t, a, c, t, t, c, a, t,
t, t, t, t, t, t, t, t,
a, a, a, c, c, a, a, a,
c, a, a, a, a, a, a, c,
c, c, a, a, a, a, c, c]

# Display the image
b = (255, 255, 255) # Άσπρο
w = (255, 192, 203) # Ρόζ
e = (0, 0, 205) # ΜεσαίουΜπλε
v = (255, 0, 0) # Κόκκινο
f = (25, 25, 112) # MidnightBlue

image2 = [
b, b, f, b, b, b, f, b,
b, f, w, f, b, f, w, f,
b, f, w, f, b, f, w, f,
f, w, w, f, f, f, w, f,
f, w, v,w, w, w, v, f,
f, w, w, w, v, w, w, f,
f,w, w, v, v, v, w, f,
b, f, f, f, f, f, f, b]


for i in range(14):
    rgb = sense.color # get the colour from the sensor    
    c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour
    b = (rgb.red, rgb.green, rgb.blue) # use the sensed colour   
    # Display the image
    sense.set_pixels(image1)
    sleep(1)

    # Display the image
    sense.set_pixels(image2)
    sleep(1)


sense.clear()




