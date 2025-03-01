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
G=(255, 255, 255)
J=(255, 255, 0)
N=(58, 255, 14)
AL=(165, 42, 42)
BD=(128, 128, 128)
BG=(0, 0, 0)

E=(77, 255, 119)
j=(255, 255, 0)
W=(165, 42, 42)
AA=(255, 255, 255)

# Zobraz obrázek
for i in range (7):
    rgb=sense.color
    c=(rgb.red,rgb.green,rgb.blue)
    
    obrazek1 = [
        c, c, c, G, c, c, J, J,
        c, c, N, G, G, c, J, J,
        c, N, N, N, G, G, c, c,
        N, N, N, N, N, G, G, G,
        G, G, AL, G, G, G, G, G,
        G, G, AL, G, G, G, c, G,
        c, c, AL, G, BD, BD, BD, BG,
        c, c, AL, G, BG, G, BG, G]
    
    obrazek2 = [
        c, E, E, E, E, E, j, j,
        c, E, E, E, E, E, j, j,
        c, E, E, W, W, E, E, AA,
        c, E, W, W, W, E, c, AA,
        c, E, W, W, E, E, c, AA,
        c, E, W, W, E, E, c, AA,
        c, AA, AA, W, W, c, c, AA,
        E, E, W, W, E, E, E, E]
    
    sense.set_pixels(obrazek1)
    sleep(2)
    sense.set_pixels(obrazek2)
    sleep(2)