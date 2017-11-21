#!/usr/bin/python3

import math

def line_get_slope_inter(line):
   ''' get slope and y intercept from 2 points
      (x1, y1, x2, y2) = line
      (slope, y_intercept) = ret
   '''

   x1, y1, x2, y2 = line
   return line_get_slope_inter_4(x1, y1, x2, y2)

def line_get_slope_inter_4(x1, y1, x2, y2):
   rise = y2 - y1
   run = x2 - x1

   slope = rise/run
   y_inter = y1 - (x1 * slope)

   return (slope, y_inter)

def line_solve_for_y(x, line_data):
   '''Solve line equation for y.
      slope, y_inter = line_data
      y = ret
   '''
   slope, y_inter = line_data
   return slope*x + y_inter


def about_eq(*vals):
   if len(vals) == 0:
      return False

   first = vals[0]
   for val in vals:
      if abs(val - first) > 0.01:
         return False
   return True


'''Find the point where 2 lines intersect'''
def line_find_intersect(l1, l2):
   slope1, y_inter1 = l1 #line_get_slope_inter(l1)
   slope2, y_inter2 = l2 #line_get_slope_inter(l2)

   b1 = slope1
   b2 = slope2

   c1 = y_inter1
   c2 = y_inter2

   x = (c2 - c1) / (b1 - b2)

   y1 = line_solve_for_y(x, l1)
   y2 = line_solve_for_y(x, l2)

   print('line intersecs:', y1, y2)
   assert(about_eq(y1, y2)) #assert(y1 == y2)

   y = y1

   return  (x, y)

'''Check if x,y in circle with radius r and origin (0, 0)'''
def is_point_in_circ(r, x, y):

   point_dist_from_origin = math.sqrt(abs(x)**2 + abs(y)**2)

   return point_dist_from_origin < r

'''solve for x or y given radius and x/y'''
def circ_solve_for_xy(r, xy):
   return math.sqrt(r**2  - xy**2)


def run(circ_r, circ_x, circ_y, lines):

   r = circ_r

   lines_good = []
   lines_data = [] #[(slope, y_intercept), ...]

   num_inside_intersecs = 0
   num_cuts = 0

   line_intersects = {}

   #for each line has coordinate [ (p1, p2), (p1, p2) ] where intersects circl
   intersections = [] #for circle


   for line in lines:
      (x1, y1, x2, y2) = line

      #x1 -= circ_x #y1 -= circ_y #x2 -= circ_x #y2 -= circ_y

      new_line = (x1 - circ_x, y1 - circ_y, x2 - circ_x, y2 - circ_y)
      lines_good.append(new_line)
      lines_data.append(line_get_slope_inter(new_line))


   for (line_coords, line_data) in zip(lines_good, lines_data):
      slope, y_inter = line_data

      b = slope
      c = y_inter

      b_square = b**2
      r_square = r**2

      inside_root = r_square + (b_square * r_square) - c**2

      try:
         z = b * math.sqrt(inside_root)
      except Exception as e:
         intersections.append(None)
         continue

      ya = b_square + 1

      y1 = (c + z)/ya
      y2 = (c - z)/ya


      x1 = circ_solve_for_xy(r, y1)
      x2 = circ_solve_for_xy(r, y2)

      p1 = (x1, y1)
      p2 = (x2, y2)

      intersections.append((p1, p2))

      pass



   #we're gonna calculate inside intersections
   for i, ld1 in enumerate(lines_data):
      for j, ld2 in enumerate(lines_data):
         if i == j:
            continue

         key = frozenset([j, i])
         val = line_intersects.get(key, None)
         if val is None:
            line_intersects[key] = line_find_intersect(ld1, ld2)
         pass

      pass


   for line_inter_key in line_intersects:
      val = line_intersects[line_inter_key]

      x, y = val
      if is_point_in_circ(r, x, y):
         print('inside 2 lines intersection:', val)
         num_inside_intersecs += 1
      else:
         print('outside 2 lines intersection:', val)

      pass

   for (inters, l_data, good_l, old_l) in zip(intersections, lines_data, lines_good, lines):
      if inters is None:
         print('\nline does not intercept circle: ', old_l)
      else:
         print('\nline ', old_l, ' intesections:', inters, '\n\n')
         num_cuts += 1
      pass


   answer = num_cuts + (num_inside_intersecs) + 1
   print('num cuts:', num_cuts, ' num_inside_line_inters:', num_inside_intersecs, ' answer:', answer)

   pass

   return lines_good, lines_data, intersections




def main():
   circ_r = 16
   circ_x = 1
   circ_y = 7

   n = 4
   lines = [
      (-15, -9, 14, -11),
      (-4, 30, -3, -20),
      (-20, 12, -10, 7),
      (17, 10, 31, 0)
   ]

   return run(circ_r, circ_x, circ_y, lines)

'''
- line = (x1, y1, x2, y2)
- we will normalize line and circle but putting circle center at 0,0 and recalculating all the lines

'''

ret = main()

