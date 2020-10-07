def run(cover, bound):
  if (cover == 'soft' or cover == 'Soft'):
    if (bound == 'yes' or bound == 'Yes'):
      print('Soft cover, perfect bound books are very popular!')
    else:
       print('Soft covers with coils or stitches are great for short books')
  if (cover == 'hard' or cover == 'Hard'):
    print('Books with hard covers can be more expensive!')