
def run(bars):
  i = 0

  while(i < bars):
    print("Charging:...", end="")
    i = i + 1
    print(i * " █ ")

  print("The battery is fully charged.")