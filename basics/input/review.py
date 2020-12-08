def run():
  import os
  debug = os.getenv('debug')
  print('What is your name human?')
  if debug == 'true':
    name = 'drone'
    print(name)
  else:
    name = input()
  print('How old are you?')
  if (debug == 'true'):
    age = int(18)
    print(age)
  else:
    age = int(input())
  print(f'Hello {name} you are {age} years old correct?')
