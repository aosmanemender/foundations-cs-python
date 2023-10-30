while True:
  try:
    num = int(input("Enter a number: "))
    break
  except Exception:
    print("***** Please enter a valid number *****")

num = str(num)

digit = "digits" if len(num) > 1 else "digit"
print(f"{num} has {len(num)} {digit}")