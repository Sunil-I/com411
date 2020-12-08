def run():
  import os
  debug = os.getenv('debug')
  even = 0
  odd = 0
  print('Please enter the first whole number.')
  if debug == 'true':
    first = int(13)
    print(first)
  else:
    first = int(input())
  print('Please enter the second whole number.')
  if debug == 'true':
    second = int(32)
    print(second)
  else:
    second = int(input())
  print('Please enter the third whole number.')
  if debug == 'true':
    third = int(32)
    print(third)
  else: 
    third = int(input())

  if (first % 2 == 0):
   even = even + 1
  else:
    odd = odd + 1

  if (second % 2 == 0):
    even = even + 1
  else:
    odd = odd + 1
  if (third % 2 == 0):
   even = even + 1
  else:
    odd = odd + 1
  print(f'There were {even} even and {odd} odd numbers.')
