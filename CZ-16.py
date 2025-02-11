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
D=(0, 0, 0)
M=(255, 255, 255)
N=(128, 128, 128)

# Vykresluje obrázek 1 (12 sekund)
for i in range(12): 
 # Ziskej barvu ze senzoru
 rgb = sense.color
 # Pouzij barvu senzoru c jako pozadi
 c = (rgb.red, rgb.green, rgb.blue)
 # VLOZIT OBRAZEK 1
 obrazek = [
  D, D, D, D, D, D, D, D,
  D, M, N, M, M, M, N, D,
  D, M, M, M, M, N, M, D,
  D, M, N, M, N, N, M, D,
  D, M, N, M, M, M, M, D,
  D, M, M, M, M, N, N, D,
  D, N, M, M, M, N, N, D,
  D, D, D, D, D, D, D, D]
 # Zobraz obrazek na displeji
 sense.set_pixels(obrazek) 

 # Cekej 1 sekundu
 sleep(1)
    
# ********************************
# Přidej proměnné s barvami a obrázek
# VLOZIT BARVY 2
D=(255, 255, 0)
Y=(0, 128, 0)
AO=(165, 42, 42)
# Vykresluje obrázek 2 (12 sekund)
for i in range(12): 
 # Ziskej barvu ze senzoru
 rgb = sense.color
 # Pouzij barvu senzoru c jako pozadi
 c = (rgb.red, rgb.green, rgb.blue)
 # VLOZIT OBRAZEK 2
 obrazek = [
  D, D, c, c, c, c, c, c,
  D, D, c, c, c, c, c, c,
  c, c, c, c, c, Y, c, c,
  c, c, c, c, Y, Y, Y, c,
  c, c, c, c, c, AO, c, c,
  c, c, c, c, c, AO, c, c,
  c, c, c, c, c, AO, c, c,
  Y, Y, Y, Y, Y, Y, Y, Y]

 # Zobraz obrazek na displeji
 sense.set_pixels(obrazek)
 # Cekej 1 sekundu
 sleep(1)
    
# Po casové limitu vymaz displej
# Vyber vlastní barvu x = (R, G, B), rozsah 0 az 255
x = (0, 0, 0)  
# Vymaz displej a nastav vlastní barvu x  
sense.clear(x)
