def run(name, age, height, weight):
  print(name, age, height, weight)
  bmi = weight / height * 2
  print(f"Hello {name}, you're currently {age} and your bmi is {bmi:.2f}")