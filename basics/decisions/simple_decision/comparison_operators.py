def run():
  import os
  debug = os.getenv('debug')
  even = 0
  odd = 0
  if debug == 'true':
    one = int(30)
    two = int(10)
    three = int(130)
    print('Please enter the first number.')
    print(one)
    print('Please enter the second number.')
    print(two)
    print('Please enter the third number.')
    print(three)

  else:
    one = int(input('Please enter the first number.'))
    two = int(input('Please enter the second number.'))
    three = int(input('Please enter the third number.'))
  if (one % 2 == 0):
   even = even + 1
  else:
    odd = odd + 1
  if (two % 2 == 0):
   even = even + 1
  else:
    odd = odd + 1
  if (three % 2 == 0):
   even = even + 1
  else:
    odd = odd + 1
  print(f'There were {even} even and {odd} odd numbers.')
