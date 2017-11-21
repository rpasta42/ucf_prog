#!/usr/bin/python3

from sympy.solvers import solve
from sympy import Symbol

#sudo ~/anaconda3/bin/conda update sympy
#~/anaconda3/bin/python3 a.py

'''
x = Symbol('x')

def check_set_default(vals, defaults):
   #FAKE TRIPLE QUOTE
   #   def example(first_name=None, last_name=None):
   #      default_first_name = 'John'
   #      default_last_name = 'Doe'
   #
   #      vals = (first_name, last_name)
   #      defaults = (default_first_name, default_last_name)
   #      (first_name, last_name) = check_set_default(vals, defaults)
   #
   #FAKE TIRPLE QUOTE

   for i, val in enumerate(vals):
      if val is None:
         vals[i] = defaults[i]

   return vals


def circle(x=None, y=None, h=None, k=None):
   #(x-h)^2 + (y-k)^2 = r^2

   x_ = Symbol('x')
   y_ = Symbol('y')

   h_ = Symbol('h')
   k_ = Symbol('k')

   vals = (x,y,h,k)
   defaults = (x_, y_, h_, k_)
   (x, y, h, k) = check_set_defaults(vals, defaults)
'''

def circle(x=Symbol('x_circ'), y=Symbol('y_circ'), h=Symbol('h_circ'), k=Symbol('k_circ'), r=Symbol('r_circ')):
   '''
      center = (h, k)
      radius = r
      point on circle = (x, y)

      r^2 = (x-h)^2 + (y-k)^2
      0 = (x-h)^2 + (y-k)^2 - r^2

   '''

   return ((x-h)**2 + (y-k)**2 - r**2)


def line(y=Symbol('y_line'), b=Symbol('b_line'), x=Symbol('x_line'), z=Symbol('z_line')):
   '''y = bx + z

   b = slope
   z = y-intercept (x coordinate)'''

   return (b*x + z) - y


def line_slope_intercept(x1, y1, x2, y2):
   rise = y2 - y1
   run = x2 - x1

   #b = slope
   slope = rise/run

   #z = y interspept
   y_intercept = line(y=y1, b=slope, x=x1)

   #y_intercept = line(y=0, b=slope, z=y_interspect)

   return slope, y_intercept

def mk_line(y=None, b=None, x=None, z=None):
   return {
      'type' : 'line',
      'y' : y,
      'b' : b,
      'x' : x,
      'z' : z
   }
   pass

def a_func(r, x, y, lines_):

   lines = []

   for (p1, p2) in lines_:
      (x1, y1) = p1
      (x2, y2) = p2
      b_slope, z_y_intercept = line_slope_intercept(x1, y1, x2, y2)
      new_line = mk_line(b=b_sloep, z=z_y_intercept)

      lines.append(line)


   pass

def run():

   lines = [
      ((-15, -9), (14, -11)),
      ((-4, 30), (-3, -20)),
      ((-20, 12), (-10, 7)),
      ((17, 10), (31, 0))
   ]

   #c1 = circle(x=1, y=7, r=16, x=0, y=0)
   c1 = circle(x=1, y=7, r=16, h=0, k=0)
   #c2 = solve(c1)

   ret = a_func(lines, c1)

   print(ret)
   return ret

ret = run()

