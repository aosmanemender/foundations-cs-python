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