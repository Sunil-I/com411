def run():
  import os
  debug = os.getenv('debug')
  if debug == 'true': 
    print('Please enter the number of lives.')
    lives = int(3)
    print(lives)
    print('Please enter the energy level?')
    energy = int(30)
    print(energy)
    print('Please enter the shield level.')
    shield = int(3)
    print(shield)
  else: 
    print('Please enter the number of lives.')
    lives = int(input())
    print('Please enter the energy level?')
    energy = int(input())
    print('Please enter the shield level.')
    shield = float(input())
  
  print('Health has been set.\n')
  print('Lives:',  "♥" * lives )
  print('Energy:', "♦" * energy)
  print('Shield:', "♦" * shield)
