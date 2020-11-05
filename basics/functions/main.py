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


from basics.functions.ascii_code import run
print (bcolors.WARNING + 'running basics/functions/ascii_code.py' + bcolors.ENDC)
char = input('Please enter a letter: ')
run(char)

from basics.functions.ascii_character import run
print (bcolors.WARNING + 'running basics/functions/ascii_character.py' + bcolors.ENDC)
print('Program Started!')
char = int(input('Please enter an ASCII code: '))
run(char)

