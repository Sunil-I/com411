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
  from basics.repetitions.for_loop.simple import run
  print(bcolors.WARNING + 'running basics/repetitions/for_loop/simple.py' + bcolors.ENDC)
  mountains = int(input('How many mountains should I display? '))
  run(mountains)

  from basics.repetitions.for_loop.count_down import run
  print(bcolors.WARNING + 'running basics/repetitions/for_loop/count_down.py' + bcolors.ENDC)
  steps = int(input('How far are we from the cave? '))
  run(steps)

  from basics.repetitions.for_loop.range import run
  print(bcolors.WARNING + 'running basics/repetitions/for_loop/range.py' + bcolors.ENDC)
  bright = int(input('What level of brightness is required? '))
  run(bright)

  from basics.repetitions.for_loop.characters import run
  print(bcolors.WARNING + 'running basics/repetitions/for_loop/characters.py' + bcolors.ENDC)
  markings = input('What strange markings do you see? ')
  run(markings)

  from basics.repetitions.for_loop.reverse import run
  print(bcolors.WARNING + 'running basics/repetitions/for_loop/reverse.py' + bcolors.ENDC)
  phrase = input('What phrase do you see? ')
  run(phrase)

  from basics.repetitions.for_loop.membership_operators import run
  print(bcolors.WARNING + 'running basics/repetitions/for_loop/membership_operators.py' + bcolors.ENDC)
  phrase = input('What phrase do you see? ')
  run(phrase)