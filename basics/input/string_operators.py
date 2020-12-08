def run():
  import os
  debug = os.getenv('debug')
  print('Please enter the number of lives.')
  if debug == 'true': 
    lives = 3
  else: 
    lives = int(input())
  print(' Please enter the energy level?')
  if debug == 'true': 
    energy = int(30)
  else: 
    energy = int(input())
  print(' Please enter the shield level.')
  if debug == 'true': 
    shield = int(3)
  else: 
    shield = float(input())
  
  print('Health has been set.\n')
  print('Lives:',  "♥" * lives )
  print('Energy:', "♦" * energy)
  print('Shield:', "♦" * shield)
