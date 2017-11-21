#!/usr/bin/python3

def get_today(n):
   if n == 1:
      return 1
   return n + get_today(n - 1)

def get_final(n):
   if n == 1:
      return 1
   return get_today(n) + get_final(n-1)


def run():

   while True:
      x = int(input(': '))

      if x == 0:
         break

      print(get_final(x))

run()

