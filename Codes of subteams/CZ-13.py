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
c=(255, 255, 255)
G=(255, 120, 53)
Y=(142, 255, 103)
AD=(0, 128, 0)
AH=(0, 0, 0)
AR=(155, 255, 80)
D=(0, 0, 255)
L=(0, 0, 0)
AB=(0, 128, 0)


for i in range(7):
    rgb=sense.color
    c=(rgb.red,rgb.green,rgb.blue)
    
    obrazek1 = [
        c, c, c, G, G, c, c, c,
        c, c, G, G, G, G, c, c,
        c, G, G, G, G, Y, Y, c,
        c, c, AD, AD, G, Y, AH, Y,
        c, AD, AD, AD, AD, Y, Y, Y,
        AR, AD, AD, AD, AD, Y, Y, c,
        c, AR, AR, AR, AR, c, c, c,
        c, AR, c, c, AR, c, c, c]
    
    obrazek2 = [
        D, D, D, D, c, c, D, D,
        L, D, L, c, c, c, c, D,
        L, L, L, D, c, c, D, L,
        AB, L, AB, D, D, D, D, L,
        L, L, L, L, L, L, L, L,
        D, L, L, L, L, L, L, L,
        D, L, D, L, D, L, D, L,
        AB, L, AB, L, AB, L, AB, L]
    
    sense.set_pixels(obrazek1)
    sleep(2)

    sense.set_pixels(obrazek2)
    sleep(2)

