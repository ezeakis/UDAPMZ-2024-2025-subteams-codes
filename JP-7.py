Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from sense_hat import SenseHat
... import time
... 
... # Nastav Sense HAT
... s = SenseHat()
... s.low_light = True
... 
... # Nastav senzor barev
... #sense.color.gain = 60 # Nastav citlivost senzoru  / comment outed by koki. 2025.02.09
... #sense.color.integration_cycles = 64 # Interval, který udává frekvenci měření ze senzoru / comment outed by koki. 2025.02.09
... 
... #廣田悠羽 / Hirota Yu
... blue1 = (3, 17, 86)
... blue2 = (18, 69, 86)
... black = (0, 0, 0)
... yellow = (110, 110, 0)
... orange = (135, 33, 0)
... nothing = (255, 255, 255)
... 
... def Shoebill():
...     B1 = blue1
...     B2 = blue2
...     B3 = black
...     Y = yellow
...     O = orange
...     N = nothing
...     logo = [
...     N, N, B1, N, B1, N, B1, N,
...     N, B1, B1, B1, B1, B1, B1, N,
...     B1, B3, B3, B1, B1, B3, B3, B1,
...     B1, B2, B3, B2, B2, B3, B2, B1,
...     B1, B1, B2, Y, Y, B2, B1, B1,
...     B1, B1, Y, Y, O, Y, B1, B1,
...     N, B1, Y, Y, O, Y, B1, N,
...     N, N, B1, Y, O, B1, N, N,
...     ]
...     return logo
... 
... images = [Shoebill]
... count = 0
... 
... while True: 
...     s.set_pixels(images[count % len(images)]())
...     time.sleep(15)
...     count += 1
    
s.clear(0, 0, 0)


