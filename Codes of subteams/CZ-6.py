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
E=(0, 0, 0)
AL=(255, 255, 0)
AS=(128, 128, 128)

# Vykresluje obrázek 1 (12 sekund)
for i in range(12): 
 # Ziskej barvu ze senzoru
 rgb = sense.color
 # Pouzij barvu senzoru c jako pozadi
 c = (rgb.red, rgb.green, rgb.blue)
 # VLOZIT OBRAZEK 1
 obrazek = [
  c, E, c, c, c, c, E, c,
  c, E, E, c, c, E, E, c,
  c, c, c, E, E, c, c, c,
  c, c, E, E, E, E, c, c,
  c, c, AL, AL, AL, AL, c, c,
  c, AS, E, E, E, E, AS, c,
  AS, AS, AL, AL, AL, AL, AS, AS,
  AS, AS, c, E, E, c, AS, AS]
 # Zobraz obrazek na displeji
 sense.set_pixels(obrazek) 

 # Cekej 1 sekundu
 sleep(1)
    
# ********************************
# Přidej proměnné s barvami a obrázek
# VLOZIT BARVY 2
E=(255, 255, 0)
W=(255, 0, 0)
AU=(0, 128, 0)
BH=(52, 255, 66)
# Vykresluje obrázek 2 (12 sekund)
for i in range(12): 
 # Ziskej barvu ze senzoru
 rgb = sense.color
 # Pouzij barvu senzoru c jako pozadi
 c = (rgb.red, rgb.green, rgb.blue)
 # VLOZIT OBRAZEK 2
 obrazek = [
  c, E, E, c, c, c, c, c,
  c, E, E, c, c, c, c, c,
  c, c, c, W, c, c, c, c,
  c, c, W, E, W, c, c, c,
  c, c, c, W, c, c, c, c,
  c, c, c, AU, c, c, c, c,
  c, c, c, AU, c, c, c, c,
  BH, BH, BH, BH, BH, BH, BH, BH]

 # Zobraz obrazek na displeji
 sense.set_pixels(obrazek)
 # Cekej 1 sekundu
 sleep(1)
    
# Po casové limitu vymaz displej
# Vyber vlastní barvu x = (R, G, B), rozsah 0 az 255
x = (0, 0, 0)  
# Vymaz displej a nastav vlastní barvu x  
sense.clear(x)
