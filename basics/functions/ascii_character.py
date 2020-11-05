def run(code):
  if (code >= 32 and code <= 126):
    print("The character represented by the ASCII value {} is: {}".format(code, chr(code)))
  else:
    print("The character cannot be displayed.")

print("Program Ended!")