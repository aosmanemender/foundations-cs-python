def selectionSort(list1):
  border = 0
  while border < len(list1)-1:
    minIndex = border
  
    for i in range(border+1, len(list1)):
      # if list1[i] < list1[minIndex]:
      if list1[i].lower() < list1[minIndex].lower():
        minIndex = i

    list1[border], list1[minIndex] = list1[minIndex], list1[border]
    border += 1
  print("->", list1)
  
list = ["aA", "b", "BD", "Bc", "D"]
selectionSort(list)