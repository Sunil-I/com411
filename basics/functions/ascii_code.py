def run(char):
  if len(char) > 1:
    print('Please enter a single character')
  else:
    print(f'The ASCII code for {char} is: {ord(char)}')
  print('Program Ended!')