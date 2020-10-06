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
# __file__ will show the script name
print(bcolors.WARNING + 'running ' + __file__  + bcolors.ENDC)

print()
print (bcolors.WARNING + 'running basics/output/simple_message.py' + bcolors.ENDC)
from basics.output.simple_message import start
start()

print()
from basics.output.multiline_message import start
print (bcolors.WARNING + 'running basics/output/multiline_message.py' + bcolors.ENDC)
start()

print()
from basics.output.escape_characters import run
print (bcolors.WARNING + 'running basics/output/escape_characters.py' + bcolors.ENDC)
run()

print()
from basics.output.show_beep import run
print (bcolors.WARNING + 'running basics/output/show_beep.py' + bcolors.ENDC)
run()

print()
from basics.output.ascii_art import run
print (bcolors.WARNING + 'running basics/output/ascii_art.py' + bcolors.ENDC)
run()

print()
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

print()
from basics.simple_decision.IF import run
print (bcolors.WARNING + 'running basics/simple_decision/IF.py' + bcolors.ENDC)
book = input('What type of book is this? ')
run(book)

print()
from basics.simple_decision.if_else import run
print (bcolors.WARNING + 'running basics/simple_decision/if_else.py' + bcolors.ENDC)
activity = input('Please enter the activity to be performed. ')
run(activity)

print()
from basics.simple_decision.if_elif_else import run
print (bcolors.WARNING + 'running basics/simple_decision/if_elif_else.py' + bcolors.ENDC)
direction = input('Towards which direction should I paint (up, down, left or right)? ')
run(direction)

print()
from basics.simple_decision.modulo_operator import run
print (bcolors.WARNING + 'running basics/simple_decision/modulo_operator.py' + bcolors.ENDC)
print('Please enter a whole number.')
num = int(input())
run(num)

print()
from basics.simple_decision.comparison_operators import run
print(bcolors.WARNING + 'running basics/simple_decision/comparison_operators.py' + bcolors.ENDC)
first = int(input('Please enter the first number. '))
second = int(input('Please enter the first number. '))
run(first, second)

print()
from basics.simple_decision.counter import run
print(bcolors.WARNING + 'running basics/simple_decision/counter.py' + bcolors.ENDC)
first = int(input('Please enter the first whole number.'))
second = int(print('Please enter the second whole number.'))
third = int(print('Please enter the third whole number.'))
run(first, second, third)