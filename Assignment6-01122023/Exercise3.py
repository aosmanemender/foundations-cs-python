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
    
  def decodedMessage(self, user_input): #O(n), n = input length
    decoded_message = ''
    for i in user_input:
      if i == "*":
        decoded_message += self.pop()
      else:
        self.push(i)
  
    while not self.isEmpty():
      decoded_message += self.pop()
  
    return decoded_message
    
def Main3():
  print("\nEnter MIB message")
  # message = input("-> ")

  stack = Stack()
  print("\n->", stack.decodedMessage("SIVLE ****** DAED TNSI ***"))

Main3()