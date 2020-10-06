def run(direction):
  if(direction == 'up' or direction == 'Up'):
    print('I am painting in the upward direction!')
  elif (direction == 'down' or direction == 'Down'):
    print('I am painting in the downward direction!')
  elif (direction == 'left' or direction == 'Left'):
    print('I am painting in the left direction!')
  elif (direction == 'right' or direction == 'Right'):
    print('I am painting in the right direction!')
  else:
    print('Please input a valid direction')
    direction = input()
    run(direction)
