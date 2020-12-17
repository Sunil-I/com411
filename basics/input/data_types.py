def run():
  import os
  debug = os.getenv('debug')
  if debug == 'true': 
    print('What is your name human?')
    name = 'drone'
    print(name)
    print('How old are you (in years)?')
    age = int(18)
    print(age)
    print('How tall are you (in meters)?')
    tall = float(12)
    print(tall)
    print('How much do you weigh (in kilograms)?')
    weight = float(85)
    print(weight)
  else: 
    print('What is your name human?')
    name = input()
    print('How old are you (in years)?')
    age = int(input())
    print('How tall are you (in meters)?')
    tall = float(input())
    print('How much do you weigh (in kilograms)?')
    weight = float(input())
  #calculating bmi 

  bmi= float(weight / (tall * tall))
  bmi = round(bmi, 2)
  print(f'Hello {name}, you are {age} years old and your bmi is {bmi}.')