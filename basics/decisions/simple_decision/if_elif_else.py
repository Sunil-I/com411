def run():
  import os
  debug = os.getenv('debug')
  print('Towards which direction should I paint (up, down, left or right)?')
  
  if (debug == 'true'):
    direction = 'up'
    print(direction)
  else: 
    direction = input()

  if (direction == 'up' or direction == 'up'):
      print('I am painting in the upward direction!')
  elif (direction == 'down' or direction == 'down'):
    print('I am painting in the downward direction!')
  elif (direction == 'left' or direction == 'Left'):
    print('I am painting in the right direction')
  elif (direction == 'right' or direction == 'Right'):
    print('I am painting in the left direction')
  else:
    print('Unable to find direction specified')