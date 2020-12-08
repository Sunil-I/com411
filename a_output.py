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
  from basics.output.simple_message import run
  run()
  print()
  from basics.output.multiline_message import run
  run()
  print()
  from basics.output.escape_characters import run
  run()
  print()
  from basics.output.ascii_art import run
  run()

execute()