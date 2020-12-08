def run():
  import os
  debug = os.getenv('debug')
  print('Please enter a whole number.')
  if (debug == 'true'):
    number = int(10)
    print(number)
  else:
    number = int(input())

  if (number % 2 == 0):
    print("\nThe number {} is an even number.".format(number))
  else:
    print("\nThe number {} is an odd number.".format(number))
