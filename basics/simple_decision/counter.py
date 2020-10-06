def run(first, second, third):
  odd = 0
  even = 0
  if (first % 2) == 0:
    even = even + 1
  else:
    odd = odd + 1  
  if (second % 2) == 0:
    even = even + 1
  else:
    odd = odd + 1  
  if (third % 2) == 0:
    even = even + 1
  else:
    odd = odd + 1 
  print(f'{odd} odd number(s) found with {even} even number(s) found.')