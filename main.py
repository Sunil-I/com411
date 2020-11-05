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
from basics.output.main import run
print (bcolors.WARNING + 'running basics/output/main.py' + bcolors.ENDC)
print()
run()

print()
from basics.input.main import run
print (bcolors.WARNING + 'running basics/input/main.py' + bcolors.ENDC)
print()
run()

print()
from basics.simple_decision.main import run
print (bcolors.WARNING + 'running basics/simple_decision/main.py' + bcolors.ENDC)
print()
run()

print()
from basics.simple_decision.nested_decision.main import run
print (bcolors.WARNING + 'running basics/simple_decision/nested_decision/main.py' + bcolors.ENDC)
print()
run()

print()
from basics.repetitions.while_loop.main import run
print (bcolors.WARNING + 'running basics/repetitions/while_loop/main.py' + bcolors.ENDC)
print()
run()


print()
from basics.repetitions.main import run
print (bcolors.WARNING + 'running basics/repetitions/main.py' + bcolors.ENDC)
print()
run()

print()
from basics.repetitions.while_loop.main import run
print (bcolors.WARNING + 'running basics/repetitions/while_loop/main.py' + bcolors.ENDC)
print()
run()

print()
from basics.repetitions.for_loop.main import run
print (bcolors.WARNING + 'running basics/repetitions/foor_loop/main.py' + bcolors.ENDC)
print()
run()




print()
print(bcolors.OKGREEN + 'Succesfully executed all scripts' + bcolors.ENDC)