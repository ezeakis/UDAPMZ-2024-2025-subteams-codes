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
L=(66, 255, 230)
T=(255, 255, 255)
AR=(123, 255, 240)
AS=(127, 255, 231)

# Vykresluje obrázek 1 (12 sekund)
for i in range(12): 
 # Ziskej barvu ze senzoru
 rgb = sense.color
 # Pouzij barvu senzoru c jako pozadi
 c = (rgb.red, rgb.green, rgb.blue)
 # VLOZIT OBRAZEK 1
 obrazek = [
  D, D, D, D, D, D, D, D,
  L, L, L, D, D, L, L, L,
  T, D, T, D, D, T, D, T,
  T, T, T, D, D, T, T, T,
  D, D, D, D, D, D, D, D,
  AR, AS, AR, AR, AR, AR, AR, AR,
  AS, AS, AS, D, D, AS, AS, AS,
  AS, AS, AS, AS, AS, AS, AS, AS]
 # Zobraz obrazek na displeji
 sense.set_pixels(obrazek) 

 # Cekej 1 sekundu
 sleep(1)
    
# ********************************
# Přidej proměnné s barvami a obrázek
# VLOZIT BARVY 2
D=(165, 42, 42)
U=(255, 188, 87)
AK=(255, 255, 255)
AL=(0, 0, 0)
AU=(255, 0, 0)
# Vykresluje obrázek 2 (12 sekund)
for i in range(12): 
 # Ziskej barvu ze senzoru
 rgb = sense.color
 # Pouzij barvu senzoru c jako pozadi
 c = (rgb.red, rgb.green, rgb.blue)
 # VLOZIT OBRAZEK 2
 obrazek = [
  D, D, D, D, D, D, D, D,
  D, D, D, D, D, D, D, D,
  D, U, U, U, U, U, U, D,
  U, U, U, U, U, U, U, U,
  U, AK, AL, U, U, AL, AK, U,
  U, U, U, AU, AU, U, U, U,
  U, U, D, U, U, D, U, U,
  U, U, D, D, D, D, U, U]

 # Zobraz obrazek na displeji
 sense.set_pixels(obrazek)
 # Cekej 1 sekundu
 sleep(1)
    
# Po casové limitu vymaz displej
# Vyber vlastní barvu x = (R, G, B), rozsah 0 az 255
x = (0, 0, 0)  
# Vymaz displej a nastav vlastní barvu x  
sense.clear(x)
