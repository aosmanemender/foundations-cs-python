# function: greetingUser
# description: displaying user greeting
import requests
from bs4 import BeautifulSoup

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

# function: validateAddedTab
# params: 
#   tab_title: title entered by the user
#   tab_url: url address entered by the user
# return: True/False
# description: validating user inputs (tab title, tab url) before adding it to the tabs dict
def validateAddedTab(tab_title, tab_url):
  valid = False

  if not tab_title:
    print("-> Tab title cannot be empty 🙂")
  elif not tab_url:
    print("-> Tab url cannot be empty 🙂")
  else:
    valid = True

  return valid

# function: openTab
# params: 
#   tabs: dictionary of tabs to be updated
# return: updated tabs dict
# description: adding a new tab to the tabs dict
def openTab(tabs):
  print("\n***** Opening a new tab *****")
  
  while True:
    tab_title = input("\nEnter the tab title: ")
    tab_url = input("Enter the tab URL: ")

    if validateAddedTab(tab_title, tab_url):
      tabs[tab_title] = tab_url
      print("\n-> Tab added successfully 👍")
      return tabs

# function: closeTab
# params:
#   tabs: dictionary of tabs to be updated
# description: removing a tab from the tabs dict
def closeTab(tabs):
  print("\n***** Closing a tab *****")

  if not tabs:
    print("\n-> There are no tabs to close 🙂")
    return

  while True:
    try:
      print("\nEnter the index of the tab you wish to close ")
      for i, elt in enumerate(tabs, 1):
        print(f"{i}. {elt} -> {tabs.get(elt).get('URL')}")
        for nested_tab_title, nested_tab_url in tabs.get(elt).get('Nested Tabs').items():
          print("\t", nested_tab_title, "->", nested_tab_url)

      tab_index = input("-> ")
      tab_index = len(tabs) if not tab_index and tab_index != 0 else int(
          tab_index)

      if tab_index in range(1, len(tabs) + 1):
        print("\nWould you like to close all nested tabs as well? if so enter 'yes' 🙂")
        closing_nested_tab = input("-> ")

        key = list(tabs.keys())[tab_index - 1]
        if closing_nested_tab.lower() != 'yes':
          for nested_tab_title, nested_tab_url in tabs.get(key).get('Nested Tabs').items():
            tab_url_dict = {
              'URL' : nested_tab_url,
              'Nested Tabs' : {}
            }
            tabs[nested_tab_title] = tab_url_dict
      else:
        print(f"\n-> Invalid index ({tab_index}) 🙂")
        continue

      tabs.pop(key)
      print("\n-> Tab removed successfully 👍")
      if tabs:
        displayTabs(tabs)
      break
    except Exception as e:
      print("\n-> Something went wrong, please try again 🙂")
      print("Exception:", e, "\n")

# function: swicthTab
# params:
#   tabs: dictionary of tabs to be searched into
# description: printing HTML content of the switched tab
# online reference: https://realpython.com/beautiful-soup-web-scraper-python/
def swicthTab(tabs):
  print("\n***** Switching to a tab *****")

  if not tabs:
    print("\n-> There are no tabs to switch to 🙂")
    return

  while True:
    try:
      print("\nEnter the index of the tab you wish to switch to ")
      for i, elt in enumerate(tabs, 1):
        print(f"{i}. {elt} -> {tabs.get(elt)}")

      tab_index = input("-> ")
      tab_index = len(tabs) if not tab_index and tab_index != 0 else int(tab_index)

      if tab_index in range(1, len(tabs) + 1):
        URL = tabs.get(list(tabs.keys())[tab_index - 1])
        print(f"\n-> Switching to tab: {URL}\n")
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")
        print(soup)
        break
      else:
        print(f"\n-> Invalid index ({tab_index}) 🙂")
    except Exception as e:
      print("\n-> Something went wrong, please try again 🙂")
      print("Exception:", e, "\n")

# function: displayTabs
# params: 
#   tabs: dictionary of tabs to be displayed
# description: printing all tabs opened
def displayTabs(tabs):
  print("\n***** Displaying all tabs *****\n")
  for tab_title, tab_url in tabs.items():
    print(f"{tab_title} : {tab_url}")
    
def openNestedTab():
  print("bye 👋 bye 👋")
def sortTabs():
  print("bye 👋 bye 👋")
def saveTabs():
  print("bye 👋 bye 👋")
def importTabs():
  print("bye 👋 bye 👋")
def exit():
  print("bye 👋 bye 👋")

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