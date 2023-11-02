def binary(n, res, count = 0):
  
  print("-> ", res)
  count += 1

  # stop @
  if res == "1"*n:
    print("all binary num of length ", n, " is: ", count)
    return
  
  for i in range(n-1, -1, -1):
    if res[i] == "0":
      res = res[:i] + "1" + res[i + 1:]
      break
    if res[i] == "1":
      res = res[:i] + "0" + res[i + 1:]
  
  binary(n, res, count)

while True:
  try:
    num = int(input("Enter a number: "))
    binary(num, "0"*num)
    break
  except Exception:
    print("***** Please enter a valid number *****")