# Colours
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def execute():
  from basics.input.user_input import run
  run()
  print()
  from basics.input.ascii_robot import run
  run()
  print()
  from basics.input.data_types import run
  run()
  print()
  from basics.input.string_operators import run
  run()
  print()
  from basics.input.review import run
  run()

execute()