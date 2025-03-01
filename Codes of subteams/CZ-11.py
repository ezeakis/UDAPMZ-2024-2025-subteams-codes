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
E=(255, 255, 0)
U=(165, 42, 42)
Y=(255, 57, 7)
AH=(255, 65, 7)
AM=(255, 87, 15)
AO=(255, 61, 2)
AQ=(255, 244, 252)
D=(0, 0, 0)

# Zobraz obrázek

for i in range(7):
    rgb=sense.color
    c=(rgb.red,rgb.green,rgb.blue)
    
    
    obrazek1 = [
      c, E, c, c, c, c, c, c,
      c, c, c, c, c, c, E, c,
      c, U, U, U, c, Y, c, c,
      U, U, U, U, U, c, AH, c,
      U, U, U, AM, AM, AO, c, c,
      U, AM, AM, AO, U, U, c, E,
      AM, AO, U, U, U, c, c, c,
      c, U, U, U, c, c, c, c]

    obrazek2 = [
            D, D, D, D, D, D, D, D,
            c, D, D, D, D, D, D, D,
            D, D, D, D, D, D, D, D,
            D, D, c, D, D, c, D, D,
            D, D, D, D, D, D, D, D,
            D, D, c, D, D, c, D, D,
            D, D, D, D, D, D, D, D,
            D, D, D, D, D, D, D, D]
        
    
    sense.set_pixels(obrazek1)
    sleep(2)
    sense.set_pixels(obrazek2)
    sleep(2)
