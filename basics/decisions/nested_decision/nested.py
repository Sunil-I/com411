def run():
  import os
  debug = os.getenv('debug')
  if debug == 'true':
    cover = 'hard'
    print('What type of cover does the book have?')
    print(cover)
  else:
    print('What type of cover does the book have?')
    cover = input()
  if cover == 'soft':
    print('Is the book perfect-bound?')
    bound = input()
    if bound == 'yes':
      print('Soft cover, perfect bound books are very popular!')
    else:
      print('Soft covers with coils or stitches are great for short books')
  if cover == 'hard':
    print('Books with hard covers can be more expensive!" should be displayed')