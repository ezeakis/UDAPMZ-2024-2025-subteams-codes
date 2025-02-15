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
G=(255, 120, 53)
Y=(142, 255, 103)
AD=(0, 128, 0)
AH=(0, 0, 0)
AR=(155, 255, 80)

# Vykresluje obrázek 1 (12 sekund)
for i in range(12): 
 # Ziskej barvu ze senzoru
 rgb = sense.color
 # Pouzij barvu senzoru c jako pozadi
 c = (rgb.red, rgb.green, rgb.blue)
 # VLOZIT OBRAZEK 1
 obrazek = [
  c, c, c, G, G, c, c, c,
  c, c, G, G, G, G, c, c,
  c, G, G, G, G, Y, Y, c,
  c, c, AD, AD, G, Y, AH, Y,
  c, AD, AD, AD, AD, Y, Y, Y,
  AR, AD, AD, AD, AD, Y, Y, c,
  c, AR, AR, AR, AR, c, c, c,
  c, AR, c, c, AR, c, c, c]
 # Zobraz obrazek na displeji
 sense.set_pixels(obrazek) 

 # Cekej 1 sekundu
 sleep(1)
    
# ********************************
# Přidej proměnné s barvami a obrázek
# VLOZIT BARVY 2
Q=(255, 0, 0)
Y=(255, 255, 0)
AG=(0, 128, 0)
# Vykresluje obrázek 2 (12 sekund)
for i in range(12): 
 # Ziskej barvu ze senzoru
 rgb = sense.color
 # Pouzij barvu senzoru c jako pozadi
 c = (rgb.red, rgb.green, rgb.blue)
 # VLOZIT OBRAZEK 2
 obrazek = [
  c, c, c, c, c, c, c, c,
  c, c, c, c, c, Q, c, c,
  c, c, Q, c, Q, Y, Q, c,
  c, Q, Y, Q, c, AG, c, c,
  c, c, AG, c, c, AG, c, c,
  c, c, AG, c, c, AG, c, c,
  c, AG, AG, AG, AG, AG, AG, c,
  c, c, c, c, c, c, c, c]

 # Zobraz obrazek na displeji
 sense.set_pixels(obrazek)
 # Cekej 1 sekundu
 sleep(1)
    
# Po casové limitu vymaz displej
# Vyber vlastní barvu x = (R, G, B), rozsah 0 az 255
x = (0, 0, 0)  
# Vymaz displej a nastav vlastní barvu x  
sense.clear(x)
