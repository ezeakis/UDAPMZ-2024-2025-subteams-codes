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
# VLOZIT BARVY 1
F=(255, 255, 255)
G=(255, 255, 0)
P=(255, 165, 0)
V=(0, 0, 0)
AB=(255, 0, 0)
AC=(165, 42, 42)

# Vykresluje obrázek 1 (12 sekund)
for i in range(12): 
 # Ziskej barvu ze senzoru
 rgb = sense.color
 # Pouzij barvu senzoru c jako pozadi
 c = (rgb.red, rgb.green, rgb.blue)
 # VLOZIT OBRAZEK 1
 obrazek = [
  c, c, F, G, c, c, c, c,
  c, F, G, G, P, c, c, c,
  c, F, V, G, G, c, c, c,
  AB, AC, G, G, P, F, F, G,
  c, c, P, F, G, G, G, P,
  c, c, F, P, F, G, P, c,
  c, c, c, G, P, P, c, c,
  c, c, c, V, c, V, c, c]
 # Zobraz obrazek na displeji
 sense.set_pixels(obrazek) 

 # Cekej 1 sekundu
 sleep(1)
    
# ********************************
# Přidej proměnné s barvami a obrázek
# VLOZIT BARVY 2
D=(255, 255, 0)
AL=(165, 42, 42)
AT=(128, 128, 128)
BJ=(28, 228, 255)
# Vykresluje obrázek 2 (12 sekund)
for i in range(12): 
 # Ziskej barvu ze senzoru
 rgb = sense.color
 # Pouzij barvu senzoru c jako pozadi
 c = (rgb.red, rgb.green, rgb.blue)
 # VLOZIT OBRAZEK 2
 obrazek = [
  D, D, D, c, c, c, c, c,
  D, D, D, c, c, c, c, c,
  D, D, D, c, c, c, c, c,
  c, c, c, c, c, c, c, c,
  c, c, AL, AL, AL, AL, c, c,
  c, AL, AT, AT, AT, AT, AL, c,
  AL, AT, AL, AL, AL, AL, AT, AL,
  AT, AL, BJ, BJ, BJ, BJ, AL, AT]

 # Zobraz obrazek na displeji
 sense.set_pixels(obrazek)
 # Cekej 1 sekundu
 sleep(1)
    
# Po casové limitu vymaz displej
# Vyber vlastní barvu x = (R, G, B), rozsah 0 az 255
x = (0, 0, 0)  
# Vymaz displej a nastav vlastní barvu x  
sense.clear(x)
