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
  from basics.repetitions.while_loop.simple import run
  print(bcolors.WARNING + 'running basics/repetitions/while_loop/simple.py' + bcolors.ENDC)
  cables = int(input('How many cables should I remove? '))
  run(cables)

  print()
  from basics.repetitions.while_loop.ascii import run
  print(bcolors.WARNING + 'running basics/repetitions/while_loop/ascii.py' + bcolors.ENDC)
  bars = int(input('How many bars should be charged? '))
  run(bars)

  print()
  from basics.repetitions.while_loop.len import run
  print(bcolors.WARNING + 'running basics/repetitions/while_loop/len.py' + bcolors.ENDC)
  chars = input('Please enter a phrase? ')
  run(chars)

  print()
  from basics.repetitions.while_loop.sum_100 import run
  print(bcolors.WARNING + 'running basics/repetitions/while_loop/sum_100.py' + bcolors.ENDC)
  run()
