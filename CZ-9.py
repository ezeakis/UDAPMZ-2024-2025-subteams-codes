# Importuj knihovny
from sense_hat import SenseHat
from time import sleep

# Nastav Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Nastav senzor barev
sense.color.gain = 60 # Nastav citlivost senzoru
sense.color.integration_cycles = 64 # Interval, který udává frekvenci měření ze senzoru

G=(0, 128, 0)
V=(0, 0, 0)
AL=(255, 0, 0)

D=(0, 0, 0)
M=(255, 255, 255)
U=(0, 0, 255)
AF=(255, 255, 0)

# Přidej proměnné s barvami a obrázek
for i in range(7):
    rgb=sense.color
    c=(rgb.red,rgb.green,rgb.blue)
    
    obrazek1 = [
        c, c, c, G, G, c, c, c,
        c, c, G, G, G, G, c, c,
        c, G, V, G, G, V, G, c,
        c, G, G, G, G, G, G, c,
        c, G, AL, G, G, AL, G, c,
        c, c, G, AL, AL, G, c, c,
        c, c, c, G, G, c, c, c,
        c, c, c, c, c, c, c, c]
    
    obrazek2=[
        D, D, D, D, D, D, D, D,
        c, c, c, c, c, c, D, D,
        c, U, c, U, U, U, c, D,
        c, U, U, U, AF, AF, c, D,
        c, U, U, U, U, U, c, D,
        c, U, c, c, c, U, c, D,
        c, c, c, D, c, c, c, c,
        D, D, D, D, c, D, D, D]   


    # Zobraz obrázek
    sense.set_pixels(obrazek1)
    sleep(2)

    sense.set_pixels(obrazek2)
    sleep(2)
