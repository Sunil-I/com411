def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print('Please select a direction ')
  dirs = directions()
  for i in range(len(dirs)):
    print(f'{i}: {dirs[i]}')