def run():
  import os
  debug = os.getenv('debug')
  print('Please enter the activity to be performed.')
  if (debug == 'true'):
    activity = 'Calculate'
    print(activity)
  else: 
    activity = input()
  if (activity == 'Calculate' or activity == 'calculate'):
    print('Performing calculations...\n')
  print('Activity completed!')