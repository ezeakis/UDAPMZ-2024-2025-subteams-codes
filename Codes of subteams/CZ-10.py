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

D=(0, 0, 0)
F=(255, 0, 0)

E=(255, 255, 255)
f=(255, 0, 0)
M=(0, 0, 0)

# Zobraz obrázek
for i in range(7):
    rgb=sense.color
    c=(rgb.red,rgb.green,rgb.blue)


    obrazek1 = [
        D, D, F, F, F, F, D, D,
        D, D, F, F, F, F, D, D,
        D, c, F, F, F, F, c, D,
        D, c, F, F, F, F, c, D,
        D, c, F, F, F, F, c, D,
        D, D, F, F, F, F, D, D,
        D, D, F, F, F, F, D, D,
        D, D, F, F, F, F, D, D]


 obrazek2 = [
      c, E, f, f, f, f, c, c,
      c, M, M, f, f, M, M, c,
      c, M, M, f, f, M, M, c,
      c, M, M, f, f, M, M, c,
      c, M, E, f, f, E, M, c,
      c, M, M, f, f, M, M, c,
      c, M, M, f, f, M, M, c,
      c, c, f, f, f, f, c, c]
    
    sense.set_pixels(obrazek1)
    sleep(2)
    sense.set_pixels(obrazek2)
    sleep(2)