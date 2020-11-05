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
  from basics.decisions.or_operator import run
  print(bcolors.WARNING + 'running basics/decisions/or_operator.py' + bcolors.ENDC)
  adventure = input('What type of adventure should I have? ')
  run(adventure)

  print()
  from basics.decisions.and_operator import run
  print(bcolors.WARNING + 'running basics/decisions/and_operator.py' + bcolors.ENDC)
  hear = input('What did I hear? ')
  see = input('What did I see? ')
  run(hear, see)