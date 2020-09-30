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
print('Running ' + __file__ );

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
