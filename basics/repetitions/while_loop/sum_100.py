def run():
  print("Calculating the sum of the first 100 numbers...")
  calc = 0
  numbers = 0
  while(numbers < 100):
    numbers = numbers + 1
    calc = calc + numbers
  print("Done! The answer is {}" .format(calc))
