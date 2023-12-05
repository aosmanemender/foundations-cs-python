class Node:
  def __init__(self,value,next):
    self.value=value
    self.next=next
class LinkedList:
  def __init__(self):
    self.head=None
    self.tail=None
    self.size=0

  def addAtHead(self,value): #O(1)
    n=Node(value,None)
    if self.size==0: # LL is empty
      self.head=n
      self.tail=n
      self.size=1
    else:
      n.next=self.head
      self.head=n
      self.size+=1

  def addAt(self, position, value): #O(n), n being the LL size
    n=Node(value,None)
    if self.size==0 or position == 0:
      self.addAtHead(value)
    else:
      count = 0
      current = self.head
      while count < position-1:
        count += 1
        current = current.next
      n.next = current.next
      current.next = n
      self.size += 1

  def deleteHead(self): #O(1)
    if self.size==0:
      return None
    elif self.size==1:
      temp=self.head.value
      self.head=None
      self.tail=None
      self.size=0
      return temp
    else:
      temp=self.head.value
      self.head=self.head.next
      self.size-=1
      return temp

  def deleteAt(self, position): #O(n), n being the LL size
    if self.size <=1 or position == 0:
      return self.deleteHead()

    count = 0
    current = self.head
    while count < position-1:
      count += 1
      current = current.next

    n = current.next
    temp = n.value

    current.next = n.next
    n.next = None

    self.size-=1
    return temp

  def printLL(self): #O(n), n being the LL size
    if self.size==0:
      print("my LL is empty")
    current=self.head
    while current!= None:
      print(current.value,"->",end=" ")
      current=current.next
    print()

def Main4():
  ll=LinkedList()

  ll.addAt(0, 0)
  ll.addAt(0, 11)
  ll.addAt(0, 76)
  ll.addAt(0, 56)
  ll.addAt(0, 12)
  ll.printLL()

  # ll.addAt(1, 1)
  # ll.printLL()
  # ll.addAt(2, 2)
  # ll.printLL()
  # ll.addAt(3, 3)
  # ll.printLL()

  ll.deleteAt(0)
  ll.printLL()
  # ll.deleteAt(3)
  # ll.printLL()

Main4()