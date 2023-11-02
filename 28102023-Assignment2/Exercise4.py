letter = input("Enter a letter: ")

Names = ["Maria", "Hala", "Ghady", "Ehsan", "Joe", "Zoe"]
counter = 0
for elt in Names:
  if(letter.lower() in elt or letter.upper() in elt):
    print("-> ", elt)
    counter+=1

if(counter == 0):
  print("No one has this letter in their name")
elif counter == 1:
  print("There is", counter, "people with this letter in their name")
else:
  print("There are", counter, "people with this letter in their name")
