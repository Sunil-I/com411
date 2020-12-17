def run():
  import os
  debug = os.getenv('debug')
  if debug == 'true':
    print('What is your name human?')
    name = 'drone'
    print(name)
    print('How old are you?')
    age = int(18)
    print(age)
  else:
    print('What is your name human?')
    name = input()
    print('How old are you?')
    age = int(input())
  print(f'Hello {name} you are {age} years old correct?')
