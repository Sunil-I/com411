def run(where, search):
  if (where == 'bedroom' or where == 'Bedroom'):
    print(f'Where in the bedroom should I look? {search}')
    if (search == 'under the bed' or search == 'Under the bed'):
      print('Found some shoes but no battery')
    else:
      print('Found some mess but no battery.')

  elif (where == 'bathroom' or where == 'Bathroom'):
    print(f'Where in the bathroom should I look? {search}')
    if (search == 'in the bathtub' or search == 'In the bathtub'):
      print('Found a rubber duck but no battery')
    else:
      print('Found a wet surface but no battery')

  elif (where == 'lab' or where == 'Lab'):
    print(f'Where in the lab should I look? {search}')

    if (search == 'on the table' or search == 'On the table'):
      print('Yes! I found my battery!')
    else:
      print('Found some tools but no battery.')

  else: 
    print('I do not know where that is but I will keep looking.')