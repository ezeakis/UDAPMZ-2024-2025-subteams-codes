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
W=(255, 0, 0)
AE=(34, 255, 15)
BF=(255, 181, 46)

# Vykresluje obrázek 1 (12 sekund)
for i in range(12): 
 # Ziskej barvu ze senzoru
 rgb = sense.color
 # Pouzij barvu senzoru c jako pozadi
 c = (rgb.red, rgb.green, rgb.blue)
 # VLOZIT OBRAZEK 1
 obrazek = [
  c, c, c, c, c, c, c, c,
  c, c, c, c, c, c, c, c,
  c, c, c, W, c, c, c, c,
  c, c, c, AE, c, c, c, c,
  c, AE, c, AE, c, AE, W, c,
  c, AE, c, AE, c, AE, c, c,
  W, AE, AE, AE, AE, AE, BF, BF,
  BF, BF, BF, AE, BF, W, BF, BF]
 # Zobraz obrazek na displeji
 sense.set_pixels(obrazek) 

 # Cekej 1 sekundu
 sleep(1)
    
# ********************************
# Přidej proměnné s barvami a obrázek
# VLOZIT BARVY 2
G=(118, 40, 255)
N=(161, 209, 255)
W=(255, 248, 12)
AZ=(155, 255, 85)
BC=(15, 255, 67)
BF=(0, 128, 0)
# Vykresluje obrázek 2 (12 sekund)
for i in range(12): 
 # Ziskej barvu ze senzoru
 rgb = sense.color
 # Pouzij barvu senzoru c jako pozadi
 c = (rgb.red, rgb.green, rgb.blue)
 # VLOZIT OBRAZEK 2
 obrazek = [
  c, c, c, G, G, c, c, c,
  c, c, N, G, G, N, c, c,
  c, G, G, W, W, G, G, c,
  c, G, G, W, W, G, G, c,
  c, c, N, G, G, N, c, c,
  c, c, c, G, G, c, c, c,
  AZ, c, AZ, BC, BC, BC, BF, AZ,
  BC, AZ, BC, BC, BC, BF, BF, BF]

 # Zobraz obrazek na displeji
 sense.set_pixels(obrazek)
 # Cekej 1 sekundu
 sleep(1)
    
# Po casové limitu vymaz displej
# Vyber vlastní barvu x = (R, G, B), rozsah 0 az 255
x = (0, 0, 0)  
# Vymaz displej a nastav vlastní barvu x  
sense.clear(x)
