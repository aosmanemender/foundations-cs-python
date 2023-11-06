items=[ ["tomato", 1], ["potato", 2], ["choco.", 3], ["soap  ", 0.5] ] 
systemCoupons = [ ["123456789", 10], ["987654321", 15], ["0000", 20], ["2023", 50] ]
# basketu = [  [2, 10, 20], [1, 10, 10], [4, 20, 10.0] ]
# totalu = 40
# couponsu = [ ["0000", 20], ["2023", 50] ]

def displaySystemItems():
  print("\n***** Displaying the available items *****\n")
  for item in items:
    print(f"{items.index(item)+1}. {item[0]} (${item[1]})")

def addItem(basket):
  displaySystemItems()
  
  while True:
    try:
      itemIndex = int(input("\nEnter the item index to add: "))

      if itemIndex == 0:
        return 0
      if itemIndex not in range(1, len(items)+1):
        print("\n***** Please enter a valid index *****")
        print("0️⃣  to return to order menu")
        continue
      else:
        break
    except Exception:
      print("\n***** Please enter a valid number *****")
      
  itemQty = int(input("Enter the desired quantity: "))
  itemPrice = 0
  
  for item in basket:
    if item[0] == itemIndex:
      item[1] += itemQty
      item[2] += itemQty * items[itemIndex - 1][1]
      itemPrice = item[2]
      break
  else:
    # a new item consists of index - quantity - price
    newItem = [ itemIndex, itemQty, itemQty * items[itemIndex - 1][1] ]
    itemPrice = itemQty * items[itemIndex - 1][1]
    basket.append(newItem)
  
  print(f"-> \"{items[itemIndex-1][0]}\" added to the basket.")
  return itemPrice
  
def displayBasket(basket):
  print("\n***** Displaying the basket *****\n")
  for item in basket:
    print(f"{basket.index(item)+1}. {items[item[0]-1][0]}\t|\t{item[1]}\t|\t${item[2]}")

def checkTotal(basket, coupons):
  print("\n***** Checking bill total price *****")
  total = 0
  discount = 0
  
  for item in basket:
    total += item[2]

  for coupon in coupons:
    discount += coupon[1]
  
  total *= (100 - discount) / 100
    
  print(f"-> Total bill: ${total}")
  return total

def checkTotalBeforeDiscount(basket):
  print("\n***** Checking bill total price before discount *****")
  total = 0

  for item in basket:
    total += item[2]

  print(f"-> Total bill: ${total}")
  return total

def checkTotalCouponsDiscount(coupons):
  print("\n***** Checking bill total coupons discount *****")
  total = 0

  for coupon in coupons:
    total += coupon[1]

  print(f"-> Total discount: %{total}")

def addCoupon(total, coupons):
  print(f"\n***** Applying a coupon on the total = ${total} *****")

  while True:
    try:
      couponCode = input("Enter your coupon code: ")
      discount = 0

      if couponCode == "0":
        break

      for coupon in coupons:
        discount += coupon[1]
        if couponCode == coupon[0]:
          print("-> Your coupon code is already applied")
          return

      for code in systemCoupons:
        if code[0] == couponCode:
          print(f"-> Your percentage discount is: %{code[1] + discount}")
          coupons.append(code)
          return

      print("\n***** Your coupon is not valid *****")
      print("0️⃣  to return to order menu")
    except Exception:
      print("\n***** Please enter a valid coupon *****")

def checkout(basket, coupons):
  displayBasket(basket)
  if coupons:
    checkTotalBeforeDiscount(basket)
    checkTotalCouponsDiscount(coupons)
  checkTotal(basket, coupons)

def newOrder():
  print("\n***** Starting a new order *****")
  basket = []
  coupons = []
  total = 0
  
  while True:
    print("\nEnter")
    print("1️⃣  to add an item")
    print("2️⃣  to check the total")
    print("3️⃣  to add a coupon")
    print("4️⃣  to checkout")
    print("5️⃣  to return to main menu")
    
    try:
      choice = int(input("-> "))
      if choice == 1:
        total += addItem(basket)
        if basket:
          displayBasket(basket)
      elif choice == 2:
        # total = checkTotal(basket, coupons)
        total = checkTotalBeforeDiscount(basket)
      elif choice == 3:
        addCoupon(total, coupons)
      elif choice == 4:
        checkout(basket, coupons)
        break
      elif choice == 5:
        break
      else:
        print("\n***** Please enter a valid number *****")
    except Exception as e:
      print("\n***** Please enter a valid number *****")
      print(e)

def closeProgram():
  print("bye 👋 bye 👋")

def main():
  while True:
    print("\nEnter")
    print("1️⃣  to start a new order")
    print("2️⃣  to close the program")
    
    try:
      choice = int(input("-> "))
      if choice == 1:
        newOrder()
      elif choice == 2:
        closeProgram()
        break
      else:
        print("\n***** Please enter a valid number *****")
    except Exception:
      print("\n***** Please enter a valid number *****")
      
main()