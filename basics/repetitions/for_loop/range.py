def run(bright):
  print('Adjusting brightness...')
  for brightness in range(2, bright + 1, 2):
    print("Beep's brightness level: ", "*" * brightness)
    print("Bop's brightness level: ", "*" * brightness)
  print('Adjustments complete!')