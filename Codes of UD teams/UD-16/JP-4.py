from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

def image_1():
  a = (255, 165, 0)
  b = (0, 255, 255)
  c = (255, 255, 0)
  list = [
  a,b,b,a,a,b,a,a,
  a,a,b,a,b,b,a,b,
  b,b,a,a,a,a,b,b,
  a,b,a,c,c,a,a,a,
  a,a,a,c,c,a,b,a,
  b,b,a,a,a,a,b,b,
  b,a,b,b,a,b,a,a,
  a,a,b,a,a,b,b,a,
  ]
  return list
def image_2():
  a = (255, 165, 0)
  b = (0, 255, 255)
  c = (255, 255, 0)
  d = (255, 255, 255)
  list = [
  a,b,b,a,a,b,a,a,
  a,a,b,a,b,b,a,b,
  b,b,a,a,a,a,b,b,
  a,b,a,c,c,a,a,a,
  a,a,a,c,c,a,b,a,
  b,b,a,a,a,a,d,d,
  b,a,b,b,a,d,d,d,
  a,a,b,a,d,d,d,d,
  ]
  return list
def image_3():
  a = (0, 255, 255)
  b = (255, 165, 0)
  c = (255, 255, 0)
  d = (255, 255, 255)
  list = [
  a,a,b,b,a,b,b,a,
  b,a,b,a,a,b,a,a,
  a,b,b,b,b,a,a,a,
  a,b,c,c,b,b,b,a,
  b,b,c,c,b,a,b,a,
  a,b,b,b,d,d,d,a,
  b,a,a,d,d,d,d,d,
  b,a,d,d,d,d,d,d
  ]
  return list
def image_4():
  a = (0, 255, 255)
  b = (255, 165, 0)
  c = (255, 255, 0)
  d = (255, 255, 255)
  list = [
  a,b,b,a,b,b,a,a,
  a,b,a,a,b,a,a,a,
  b,b,b,b,a,a,a,a,
  b,c,c,b,b,b,a,a,
  b,c,c,b,a,b,a,a,
  b,b,b,d,d,d,a,a,
  a,a,d,d,d,d,d,a,
  a,d,d,d,d,d,d,d
  ]
  return list
def image_5():
  a = (255, 165, 0)
  b = (0, 255, 255)
  c = (255, 255, 255)
  list = [
  a,a,b,b,c,c,b,b,
  a,b,b,c,c,c,c,c,
  b,b,b,b,c,c,c,b,
  a,a,b,b,b,b,b,b,
  b,a,b,b,b,b,c,c,
  c,c,b,b,b,c,c,c,
  c,c,c,b,b,b,c,c,
  c,c,c,b,b,b,b,b
  ]
  return list
def image_6():
  a = (0, 255, 255)
  b = (0, 0, 255)
  c = (255, 255, 255)
  list = [
  a,a,a,a,b,a,b,b,
  c,c,a,a,a,a,b,b,
  c,a,a,a,a,b,b,b,
  a,a,a,a,a,a,b,b,
  c,c,a,a,b,a,a,b,
  c,c,c,c,a,a,b,b,
  c,c,c,a,a,b,b,b,
  a,a,a,a,a,a,b,b,
  ]
  return list
def image_7():
  a = (0, 255, 255)
  b = (0, 0, 255)
  c = (255, 255, 0)
  list = [
  a,a,b,a,b,b,b,b,
  a,a,a,a,b,c,b,b,
  a,a,a,b,b,b,b,c,
  a,a,a,a,c,b,b,b,
  a,a,b,a,b,b,c,b,
  a,a,a,a,b,b,b,b,
  a,a,a,b,b,c,b,b,
  a,a,a,a,b,b,b,c
  ]
  return list
def image_8():
  a = (0, 255, 255)
  b = (0, 0, 255)
  c = (255, 255, 0)
  list = [
  a,b,b,b,b,c,b,b,
  a,b,c,b,b,b,b,c,
  b,b,b,b,c,b,b,b,
  a,c,b,b,b,b,c,b,
  a,a,b,c,b,b,b,b,
  a,b,b,b,b,c,b,b,
  b,b,c,b,b,b,b,c,
  a,b,b,b,b,b,b,b
  ]
  return list
def image_9():
  a = (0, 0, 255)
  b = (255, 255, 0)
  list = [
  a,a,a,a,a,a,a,a,
  a,b,a,b,b,b,a,a,
  a,a,a,a,b,b,b,a,
  b,a,a,a,a,b,b,b,
  a,a,a,a,a,b,b,b,
  a,a,a,a,b,b,b,a,
  a,b,a,b,b,b,a,a,
  a,a,a,a,a,a,a,a
  ]
  return list
def image_10():
  a = (0, 0, 255)
  b = (255, 255, 0)
  list = [
  a,a,a,a,a,a,a,a,
  a,b,b,b,a,a,a,b,
  a,a,b,b,b,a,a,a,
  a,a,a,b,b,b,a,a,
  a,a,a,b,b,b,a,a,
  a,a,b,b,b,a,a,b,
  a,b,b,b,a,a,a,a,
  a,a,a,a,a,b,a,a
  ]
  return list
def image_11():
  a = (0, 0, 255)
  b = (0, 255, 255)
  c = (255, 255, 0)
  list = [
  a,a,a,a,a,a,a,b,
  a,a,a,a,a,a,b,b,
  c,a,a,a,a,b,a,b,
  c,c,a,a,a,a,b,b,
  c,c,a,a,a,b,a,b,
  c,a,a,a,a,a,b,b,
  a,a,a,a,a,b,a,b,
  a,a,a,a,a,a,b,b
  ]
  return list
def image_12():
  a = (0, 0, 255)
  b = (0, 255, 255)
  c = (255, 165, 0)
  d = (255, 255, 0)
  e = (0, 128, 0)
  list = [
  a,a,b,b,b,b,b,b,
  a,b,b,b,b,b,b,b,
  b,a,b,b,c,b,b,c,
  a,b,b,b,c,c,b,c,
  b,a,b,b,b,b,c,c,
  a,b,b,c,c,b,c,d,
  b,a,b,b,e,e,e,e,
  a,b,e,e,e,e,e,e,
  ]
  return list
def image_13():
  a = (0, 255, 255)
  b = (255, 165, 0)
  c = (255, 255, 0)
  d = (0, 128, 0)
  list = [
  a,b,b,a,b,b,a,a,
  a,b,a,a,b,a,a,a,
  b,b,b,b,a,a,a,a,
  b,c,c,b,b,b,a,a,
  b,c,c,b,a,b,a,a,
  b,b,b,b,a,a,a,a,
  d,d,d,d,b,b,a,a,
  d,d,d,d,d,b,a,a
  ]
  return list
def image_14():
  a = (0, 255, 255)
  b = (255, 165, 0)
  c = (255, 255, 0)
  d = (0, 128, 0)
  list = [
  a,a,b,b,a,b,b,a,
  b,a,b,a,a,b,a,a,
  a,b,b,b,b,a,a,a,
  a,b,c,c,b,b,b,a,
  b,b,c,c,b,a,b,a,
  a,b,b,b,b,a,a,a,
  d,a,a,b,a,b,b,a,
  d,d,b,b,a,a,b,a
  ]
  return list
images = [image_1,image_2,image_3,image_4,image_5,image_6,image_7,image_8,image_9,image_10,image_11,image_12,image_13,image_14]
count = 0
for i in range(14):
  s.set_pixels(images[i % len(images)]())
  time.sleep(1)
