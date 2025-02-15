# Importuj knihovny
from sense_hat import SenseHat
from time import sleep

# Nastav Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Nastav senzor barev
sense.color.gain = 60 # Nastav citlivost senzoru
sense.color.integration_cycles = 64 # Interval, který udává frekvenci měření ze senzoru

# Přidej proměnné s barvami a obrázek
c=(0, 0, 0)
G=(255, 120, 53)
Y=(142, 255, 103)
AD=(0, 128, 0)
AH=(0, 0, 0)
AR=(155, 255, 80)

for i in range(28):
    rgb=sense.color
    c=(rgb.red,rgb.green,rgb.blue)
    
    obrazek = [
      c, c, c, G, G, c, c, c,
      c, c, G, G, G, G, c, c,
      c, G, G, G, G, Y, Y, c,
      c, c, AD, AD, G, Y, AH, Y,
      c, AD, AD, AD, AD, Y, Y, Y,
      AR, AD, AD, AD, AD, Y, Y, c,
      c, AR, AR, AR, AR, c, c, c,
      c, AR, c, c, AR, c, c, c]
    
    sense.set_pixels(obrazek)
    sleep(1)
# Zobraz obrázek

