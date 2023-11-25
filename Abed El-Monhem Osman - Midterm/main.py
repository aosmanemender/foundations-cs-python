import requests
from bs4 import BeautifulSoup

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

# function: openTab
# params:
#   tabs: dictionary of tabs to be updated
# description: adding a new tab to the tabs dict
def openTab(tabs):
  print("\n***** Opening a new tab *****")

  while True:
    tab_title = input("\nEnter the tab title: ")
    tab_url = input("Enter the tab URL: ")

    if validateAddedTab(tab_title, tab_url):
      tab_url_dict = {'URL': tab_url, 'Nested Tabs': {}}
      tabs[tab_title] = tab_url_dict
      print("\n-> Tab added successfully 👍\n")
      displayTabsIndexed(tabs)
      break

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

# function: displayTabsIndexed
# params:
#   tabs: dictionary of tabs to be printed
# description: displaying all tabs with index number to be picked by the user
def displayTabsIndexed(tabs):
  for i, key in enumerate(tabs, 1):
    print(f"{i}. {key} -> {tabs.get(key).get('URL')}")

# function: displayParentTabsIndexed
# params:
#   tabs: dictionary of tabs to be printed
# description: displaying only parent tabs with index number to be picked by the user
def displayParentTabsIndexed(tabs):
  for i, key in enumerate(tabs, 1):
    nested_tabs = tabs.get(key).get('Nested Tabs')
    if nested_tabs:
      print(f"{i}. {key} -> {tabs.get(key).get('URL')}")

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
      print("\nEnter the index of the tab you wish to close: \n")
      displayTabsIndexed(tabs)

      tab_index = input("-> ")
      tab_index = len(tabs) if not tab_index and tab_index != 0 else int(
          tab_index)

      if tab_index in range(1, len(tabs) + 1):
        key = list(tabs.keys())[tab_index - 1]
        
        # remove child index from the parent
        child = tabs.get(key).get('Nested Tabs') is None
        if child:
          for tab in tabs:
            nested_tabs = tabs.get(tab).get('Nested Tabs')
            if nested_tabs:
              if tab_index-1 in nested_tabs:
                nested_tabs.remove(tab_index - 1)
              for index in range(len(nested_tabs)):
                nested_tabs[index] -= 1
        
        # remove child tab
        tabs.pop(key)
        print(f"\n-> Tab {key} closed successfully 👍")
        break
      else:
        print(f"\n-> Invalid index ({tab_index}) 🙂")
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
      print("\nEnter the index of the tab you wish to switch to: \n")
      displayTabsIndexed(tabs)

      tab_index = input("-> ")
      tab_index = len(tabs) if not tab_index and tab_index != 0 else int(tab_index)

      if tab_index in range(1, len(tabs) + 1):
        URL = tabs.get(list(tabs.keys())[tab_index - 1]).get('URL')
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

  if not tabs:
    print("-> There are no tabs to display 🙂")
    return

  for key in tabs:
    nested_tabs = tabs.get(key).get('Nested Tabs')
    if nested_tabs is not None:
      print(f"{key} -> {tabs.get(key).get('URL')}")
      for nt in nested_tabs:
        print("\t", list(tabs.keys())[nt], "->", tabs.get(list(tabs.keys())[nt]).get('URL'))

# function: openNestedTab
# params:
#   tabs: dictionary of tabs to be updated
# description: adding a new nested tab to tabs dictionary
def openNestedTab(tabs):
  print("\n***** Opening nested tab *****")

  if not tabs:
    print("\n-> There are no tabs to create nested tabs from 🙂")
    return

  while True:
    try:
      print("\nEnter the index of the parent tab where you want to insert additional tabs: \n")
      displayParentTabsIndexed(tabs)

      parent_tab_index = int(input("-> "))

      if parent_tab_index in range(1, len(tabs) + 1):
        nested_tabs = tabs.get(list(tabs.keys())[parent_tab_index - 1]).get('Nested Tabs')
        if nested_tabs:
          nested_tab_title = input("\nEnter the nested tab title: ")
          nested_tab_url = input("Enter the nested tab URL: ")

          if validateAddedTab(nested_tab_title, nested_tab_url):
            # adding new nested tab to tabs dict and its index to parent tab
            tabs[nested_tab_title] = {'URL': nested_tab_url}
            nested_tabs.append(len(tabs) - 1)
            print("\n-> Nested-Tab added successfully 👍\n")
            print(tabs.get(list(tabs.keys())[parent_tab_index - 1]))
            break
        else:
          print("\n-> You can not add a nested tab to a child tab 🙂")

        
      else:
        print(f"\n-> Invalid index ({parent_tab_index}) 🙂")
    except Exception as e:
      print("\n-> Something went wrong, please try again 🙂")
      print("Exception:", e, "\n")    


def sortTabs():
  print("bye 👋 bye 👋")
def saveTabs():
  print("bye 👋 bye 👋")
def importTabs():
  print("bye 👋 bye 👋")
def exit():
  print("bye 👋 bye 👋")

# only for testing purpose
def initializeTabsDictionary():
  tabs = {}
  tabs["Tab 1"] = "https://www.google.com"
  tabs["Tab 2"] = "https://www.youtube.com"
  tabs["Tab 3"] = "https://www.facebook.com"
  tabs["Tab 4"] = "https://www.twitter.com"
  tabs["Tab 5"] = "https://www.instagram.com"
  tabs = {
    'Tab 1': 'https://www.google.com',
    'Tab 2': 'https://www.youtube.com',
    'Tab 3': 'https://www.facebook.com',
    'Tab 4': 'https://www.twitter.com',
    'Tab 5': 'https://www.instagram.com'
  }
  tabs = {
    'Tab 1': { 
        'URL': 'https://www.google.com',
        'Nested Tabs': { 
          'Nested tab 1.1': 'https://www.google.com/search?q=python',
          'Nested tab 1.2': 'https://www.google.com/search?q=java',
          'Nested tab 1.3': 'https://www.google.com/search?q=c++',
          'Nested tab 1.4': 'https://www.google.com/search?q=javascript',
          'Nested tab 1.5': 'https://www.google.com/search?q=php',
        }
     },
    'Tab 2': {
      'URL': 'https://www.youtube.com',
      'Nested Tabs': {
        'Nested tab 2.1': 'https://www.youtube.com/results?search_query=python',
        'Nested tab 2.2': 'https://www.youtube.com/results?search_query=java',
        'Nested tab 2.3': 'https://www.youtube.com/results?search_query=c++',
        'Nested tab 2.4': 'https://www.youtube.com/results?search_query=javascript',
        'Nested tab 2.5': 'https://www.youtube.com/results?search_query=php',
      }
    },
    'Tab 3': {
      'URL': 'https://www.facebook.com',
      'Nested Tabs': {
        'Nested tab 3.1': 'https://www.facebook.com/search?q=python',
        'Nested tab 3.2': 'https://www.facebook.com/search?q=java',
        'Nested tab 3.3': 'https://www.facebook.com/search?q=c++',
        'Nested tab 3.4': 'https://www.facebook.com/search?q=javascript',
        'Nested tab 3.5': 'https://www.facebook.com/search?q=php',
      }
    },
    'Tab 4': {
      'URL': 'https://www.twitter.com',
      'Nested Tabs': {
        'Nested tab 4.1': 'https://www.twitter.com/search?q=python',
        'Nested tab 4.2': 'https://www.twitter.com/search?q=java',
        'Nested tab 4.3': 'https://www.twitter.com/search?q=c++',
        'Nested tab 4.4': 'https://www.twitter.com/search?q=javascript',
        'Nested tab 4.5': 'https://www.twitter.com/search?q=php',
      }
    },
    'Tab 5': {
      'URL': 'https://www.instagram.com',
      'Nested Tabs': {
        'Nested tab 5.1': 'https://www.instagram.com/search?q=python',
        'Nested tab 5.2': 'https://www.instagram.com/search?q=java',
        'Nested tab 5.3': 'https://www.instagram.com/search?q=c++',
        'Nested tab 5.4': 'https://www.instagram.com/search?q=javascript',
        'Nested tab 5.5': 'https://www.instagram.com/search?q=php',
      }
    }
  }
  return tabs

def menu():
  tabs = initializeTabsDictionary()
  greetingUser()
  
  while True:
    displayMenu()

    try:
      choice = int(input("-> "))
      if choice == 1:
        openTab(tabs)
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