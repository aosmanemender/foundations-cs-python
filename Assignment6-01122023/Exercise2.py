# balanced () {} []
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

  # if ( before ) -> False
  # if { before } -> False
  # if [ before ] -> False
  # 
  # ] need [ -> True else -> False
  # ) need ( -> True else -> False
  # } need { -> True else -> False
  #
  #    (1+2)-3*[41+6]
  # -> ]6+14[*3-)2+1(
  # ] [ ) ( -> True
  # 
  #    (1+2)-3*[41+6}
  # -> }6+14[*3-)2+1(
  # } [ -> False
  #
  #    (1+2)-3*[41+6
  # -> 6+14[*3-)2+1(
  # [ -> False
  #
  #    (1+2)-3*]41+6[
  # -> [6+14]*3-)2+1(
  # [ -> False
  #
  #    (1+[2-3]*4{41+6})
  def isBalanced(self): #O(n), n = stack size
    parenthesis = ''
    brackets = ''
    braces = ''

    valid = False
    while not self.isEmpty():
      character = self.pop()
      if character in '()':
        parenthesis += character
        if parenthesis == '(':
          return False
      elif character in '[]':
        brackets += character
        if brackets == '[':
          return False
      elif character in '{}':
        braces += character
        if braces == '{':
          return False

    valid = parenthesis in ('', ')(') and brackets in ('', '][') and braces in ('', '}{')

    return valid

def Main2():
  print("\nEnter your expression")
  user_expression = input("-> ")

  stack = Stack()
  stack.pushCharsToStack(user_expression)

  if stack.isBalanced():
    print("\nBalanced 🙂")
  else:
    print("\nNot Balanced 🙂")

while True:
  Main2()