# Colours
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

print(f'{OKGREEN}Welcome to com411 code runner.{ENDC}\n')
print(f'{OKGREEN}Running Part A Output code.{ENDC}')
from a_input import execute
execute()

print()
print(f'{OKGREEN}Running Part A Input code.{ENDC}')
from a_output import execute
execute()

print()
print(f'{OKGREEN}Running Part A Simple decisions code.{ENDC}')
from a_simple_decision import execute
execute()