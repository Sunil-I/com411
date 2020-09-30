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
import sys
# __file__ will show the script name
print(bcolors.OKBLUE + bcolors.WARNING + 'running ' + __file__  + bcolors.ENDC);

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
print (bcolors.WARNING + 'running basica/input/user_input.py' + bcolors.ENDC)
print('What is your name?')
run(sys.argv[1])

print()
from basics.input.ascii_robot import run
print (bcolors.WARNING + 'running basics/input/ascii_robot.py' + bcolors.ENDC)
print('What character should I use for my eye? e.g 0')
run(sys.argv[2])

print()
from basics.input.user_age import run
print (bcolors.WARNING + 'running basics/input/user_age.py' + bcolors.ENDC)
print('How old are you?')
run(sys.argv[3])

print()
from basics.input.data_types import run
print (bcolors.WARNING + 'running basics/input/data_types.py' + bcolors.ENDC)
print('What is your name human? ')
print('How old are you (in years)? ')
print('How tall are you (in meters)? ')
print('How much do you weigh (in kilograms)? ')
run(sys.argv[4], sys.argv[5], int(sys.argv[6]), int(sys.argv[7]))
