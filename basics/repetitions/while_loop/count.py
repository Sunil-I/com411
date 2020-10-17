def run(live):
  i = 0
  while (i < live):
    print('Avoiding...', end = '')
    print(f'Done! {i+1} live cable avoided!')
    i = i + 1
  print("All live cables have been avoided.")