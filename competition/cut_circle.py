#!/usr/bin/python3


def run():
   data = input('Enter data: ')
   ds = data.split(' ')

   r = int(ds[0])
   x = int(ds[1])
   y = int(ds[2])
   n = int(ds[3])

   lines = []

   for x in range(0, n):
      data = input('Lines: ')
      ld = data.split(' ')

      x1 = int(ld[0])
      y1 = int(ld[1])
      x2 = int(ld[2])
      y2 = int(ld[3])
      lines.append((x1, y1, x2, y2))

   print(lines)

   cut_circle(r, x, y, n, lines)

def get_slope(x1, y1, x2, y2):
   rise = y2 - y1
   run = x2 - x1

   return rise/run

def get_y_inter(x1, y1, x2, y2, slope):

   x1 /= slope
   y1


def cut_circle(r, x, y, n, lines):


   pass


