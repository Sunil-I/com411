# Import color classes
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def run(): 
  from basics.input.user_input import run
  print (bcolors.WARNING + 'running basics/input/user_input.py' + bcolors.ENDC)
  name = input('What is your name? ')
  run(name)

  print()
  from basics.input.ascii_robot import run
  print (bcolors.WARNING + 'running basics/input/ascii_robot.py' + bcolors.ENDC)
  eye = input('Input one character e.g 0 ')
  run(eye)

  print()
  from basics.input.user_age import run
  print (bcolors.WARNING + 'running basics/input/user_age.py' + bcolors.ENDC)
  age = input('Please enter an age ')
  run(age)

  print()
  from basics.input.data_types import run
  print (bcolors.WARNING + 'running basics/input/data_types.py' + bcolors.ENDC)
  name_beep = input('What is your name human? ')
  age_beep = input('How old are you (in years)? ')
  height_beep = int(input('How tall are you (in meters)? '))
  weight_beep = int(input('How much do you weigh (in kilograms)? '))
  run(name_beep, age_beep, height_beep, weight_beep)

  print()
  from basics.input.string_operators import run
  print (bcolors.WARNING + 'running basics/input/string_operators.py' + bcolors.ENDC)
  lives = int(input('Please enter the number of lives. '))
  energy_levels = int(input('Please enter the energy level. '))
  shield_levels = int(input('Please enter the shield level. '))
  run(lives, energy_levels, shield_levels)

  print()
  from basics.input.review import run
  print (bcolors.WARNING + 'running basics/input/review.py' + bcolors.ENDC)
  name = input('What is your name human? ')
  age = input('What is your age human? ')
  height = input('How tall are you human? in metres ')
  weight = input('How much do you weigh human? ')
  health = int(input('Please enter the number of lives. '))
  shield = int(input('Please enter the shield level. '))
  run(name, age, height, weight, health, shield)
