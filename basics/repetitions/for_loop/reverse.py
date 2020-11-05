def run(phrase):
  print('Reversing...')
  dummy = ""
  for i in range(len(phrase) , 0, -1):
    dummy += phrase[i-1]
  print(f'The phrase is: {dummy}')