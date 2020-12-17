def run():
  import os
  debug = os.getenv('debug')
  # Ask user to enter their name
  if (debug == 'true'):
    print("What is your name human?")
    name = "drone"
    print(name)
  else:
    print("What is your name human?")
    name = input()
  print("It is nice to meet you human", name)
