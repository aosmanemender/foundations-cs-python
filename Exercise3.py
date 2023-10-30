min = max = 0

while True:
  try:
    N1 = int(input("Enter the 1st number: "))
    N2 = int(input("Enter the 2nd number: "))
    break
  except Exception:
    print("***** Please enter a valid number *****")

list1 = [54, 76, 2, 4, 98, 100]
list1.sort()
print(list1)

print("\nThe range of values that are between {} and {} included is:".format(
    N1, N2))
for elt in list1:
  if (elt >= N1 and elt <= N2) or (elt <= N1 and elt >= N2):
    print("-> ", elt)

# print(isinstance(min, int))