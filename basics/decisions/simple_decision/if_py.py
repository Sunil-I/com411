def run():
  import os
  debug = os.getenv('debug')
  print('What type of book is this?')
  if (debug == 'true'):
    book = 'adventure'
  else:
    book = input()
  if (book == 'adventure' or book == 'Adventure'):
    print('I like adventure books!\n')
  print('Finished reading book.')