# Colours
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
import os
debug = os.getenv('debug')

def execute():
  from basics.decisions.simple_decision.if_py import run
  run()
  print()
  from basics.decisions.simple_decision.if_else import run
  run()
  print()
  from basics.decisions.simple_decision.if_elif_else import run
  run()

if (debug == 'true'):
  execute()