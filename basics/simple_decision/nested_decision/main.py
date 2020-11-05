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
  from basics.simple_decision.nested_decision.nested import run
  print(bcolors.WARNING + 'running basics/simple_decision/nested_decision/nested.py' + bcolors.ENDC)
  cover = input('What type of cover does the book have? ')
  bound = input('Is the book perfect-bound? ')
  run(cover, bound)

  print()
  from basics.simple_decision.nested_decision.nestception import run
  print(bcolors.WARNING + 'running basics/simple_decision/nested_decision/nestception.py' + bcolors.ENDC)
  where = input('Where should I look? ')
  run(where)

