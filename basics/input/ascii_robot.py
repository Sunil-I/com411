def run():
  print('Please enter a character for the eye')
  import os
  debug = os.getenv('debug')
  print("What is your name human?")
  if (debug == 'true'):
    eye = "0"
  else:
    eye = input()
  print("Beep's expression is now as follows:")
  print('  ##########')
  print(f'  #  {eye}  {eye}  #')
  print('  #  ----  #')
  print('  ##########')
