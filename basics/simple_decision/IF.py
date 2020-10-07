# Only things after the usage of : should be indented here.
def run(answer):
  if (answer == ''):
    print('Please input a book type!')
    quit()
  if (answer == 'adventure' or answer == 'Adventure'):
      print('I like adventure books!')
  print('Finished reading book.')
      