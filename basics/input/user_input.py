def run():
  import os
  debug = os.getenv('debug')
  # Ask user to enter their name
  print("What is your name human?")
  if (debug == 'true'):
    name = "drone"
    print(name)
  else:
    name = input()
  print("It is nice to meet you human", name)
