# palindrom
class Stack:
  def __init__(self) :
    self.items=[]

  def isEmpty(self): #O(1)
    return len(self.items) == 0

  def push(self,value): #O(1)
    self.items.append(value)

  def pop(self): #O(1)
    if self.isEmpty():
      return ''
    return self.items.pop()
    
  def pushCharsToStack(self, user_input): #O(n), n = input length
    for i in user_input:
      self.push(i)
  
  def popCharsFromStack(self): #O(n), n = input length
    new_input = ""
    while not self.isEmpty():
      new_input += self.pop()
    return new_input
  
def Main(): #O(n), n = input length
  print("\nEnter your input")
  user_input = input("-> ")

  stack = Stack()
  stack.pushCharsToStack(user_input)
  new_input = stack.popCharsFromStack()

  if new_input == user_input:
    print("\nPalindrom 🙂")
  else:
    print("\nNot Palindrom 🙂")

while True:
  Main()