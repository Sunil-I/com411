def run():
  import os
  debug = os.getenv('debug')
  print('What is your name human?')
  if debug == 'true': 
    name = 'drone'
  else: 
    name = input()
  print('How old are you (in years)?')
  if debug == 'true': 
    age = int(18)
  else: 
    age = int(input())
  print('How tall are you (in meters)?')
  if debug == 'true': 
    tall = float(1.80)
  else: 
    tall = float(input())
  print('How much do you weigh (in kilograms)?')
  if debug == 'true': 
    weight = float(85)
  else: 
    weight = float(input())
  #calculating bmi 

  bmi= float(weight / (tall * tall))
  bmi = round(bmi, 2)
  print(f'{name} you are {age} years old and your bmi is {bmi}.')