def run(where):
  if (where == 'bedroom' or where == 'Bedroom'):
    where_detailed = input('Where in the bedroom should I look? ')
    if (where_detailed == 'under the bed' or where_detailed == 'Under the bed'):
      print('Found some shoes but no battery')
    else:
      print('Found some mess but no battery.')

  elif (where == 'bathroom' or where == 'Bathroom'):
    where_detailed = input('Where in the bathroom should I look? ')
    if (where_detailed == 'in the bathtub' or where_detailed == 'In the bathtub'):
      print('Found a rubber duck but no battery')
    else:
      print('Found a wet surface but no battery')

  elif (where == 'lab' or where == 'Lab'):
    where_detailed = input('Where in the lab should I look? ')

    if (where_detailed == 'on the table' or where_detailed == 'On the table'):
      print('Yes! I found my battery!')
    else:
      print('Found some tools but no battery.')

  else: 
    print('I do not know where that is but I will keep looking.')