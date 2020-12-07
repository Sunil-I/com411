def run():
  import os
  debug = os.getenv('debug')
  # Ask user to enter their name
  print("What is your name human?")
  if (debug == 'true'):
    name = "drone"
  else:
    name = input()
  print("It is nice to meet you human", name)
