def run(phrase):
  dummy = ""
  for i in phrase:
    dummy = i + dummy
  print(f'The phrase is: {dummy}')