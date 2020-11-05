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
  num = int(input('Please enter a whole number. '))
  run(num)

  print()
  from basics.simple_decision.comparison_operators import run
  print(bcolors.WARNING + 'running basics/simple_decision/comparison_operators.py' + bcolors.ENDC)
  first = int(input('Please enter the First number. '))
  second = int(input('Please enter the Second number. '))
  run(first, second)

  print()
  from basics.simple_decision.counter import run
  print(bcolors.WARNING + 'running basics/simple_decision/counter.py' + bcolors.ENDC)
  first = input('Please enter the first whole number. ')
  second = input('Please enter the second whole number. ')
  third = input('Please enter the third whole number. ')
  run(int(first), int(second), int(third))