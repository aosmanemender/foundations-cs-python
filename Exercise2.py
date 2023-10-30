N = 0
while True:
  try:
    N = int(input("Enter a number: "))
    if(N < 0):
      continue
    break
  except Exception:
    print("***** Please enter a valid number *****")

for i in range(N):
  print((i+1) * "*")