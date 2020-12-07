# Colours
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
import os

print(os.getenv('path'))
print(f'{OKGREEN}Welcome to com411 code runner.{ENDC}\n')
print(f'{OKGREEN}Running Part A code.{ENDC}')
from a import execute
execute()