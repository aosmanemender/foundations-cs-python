# function: greetingUser
# description: displaying user greeting
def greetingUser():
  print("\n***** Hello, And Welcome *****\n")

# function: displayMenu
# description: displaying the main menu with a variety of options
def displayMenu():
  print("\n***** Main Menu *****\n")
  print("Please select an option")
  print("1. Open Tab")
  print("2. Close Tab")
  print("3. Switch Tab")
  print("4. Display All Tabs")
  print("5. Open Nested Tab")
  print("6. Sort All Tabs")
  print("7. Save Tabs")
  print("8. Import Tabs")
  print("9. Exit")

def initializeTabsDictionary():
  tabs = {}
  tabs["Tab 1"] = "https://www.google.com"
  tabs["Tab 2"] = "https://www.youtube.com"
  tabs["Tab 3"] = "https://www.facebook.com"
  tabs["Tab 4"] = "https://www.twitter.com"
  tabs["Tab 5"] = "https://www.instagram.com"
  return tabs

def menu():
  tabs = initializeTabsDictionary()
  greetingUser()
  
  while True:
    displayMenu()

    try:
      choice = int(input("-> "))
      if choice == 1:
        tabs = openTab(tabs)
        displayTabs(tabs)
      elif choice == 2:
        closeTab(tabs)
      elif choice == 3:
        swicthTab()
      elif choice == 4:
        displayTabs(tabs)
      elif choice == 5:
        openNestedTab()
      elif choice == 6:
        sortTabs()
      elif choice == 7:
        saveTabs()
      elif choice == 8:
        importTabs()
      elif choice == 9:
        exit()
        break
      else:
        print("\n-> Please enter a valid number 🙂")
    except Exception as e:
      print("\n-> Something went wrong, please try again 🙂")
      print("Exception:", e, "\n")

menu()