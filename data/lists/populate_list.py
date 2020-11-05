def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print('Please select a direction')
  path = directions()
  for i in range(len(path)):
    print(f'{i}: {path[i]}')
  direction = input()
  print(f'You have chosen {direction}')
  return path[int(direction)]

def run():
  route = []
  print('Working out escape route...')
  for count in range(5):
    route.append(menu())
  print(f'Escape route: {route}')