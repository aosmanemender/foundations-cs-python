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
      tabs[tab_title] = {
        'Tab Index' : len(tabs),
        'URL': tab_url,
        'Nested Tabs': []
      }
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
      if not tab_index and tab_index != 0:
        tab_index = findLastOpenedTab(tabs)
      else:
        tab_index = int(tab_index)

      if tab_index in range(1, len(tabs) + 1):
        key = list(tabs.keys())[tab_index - 1]
        child = tabs.get(key).get('Nested Tabs') is None
                
        # decrement tab indexes by 1
        for tab in tabs:
          if tabs[tab]['Tab Index'] > tab_index - 1:
            tabs[tab]['Tab Index'] -= 1
          nested_tabs = tabs.get(tab).get('Nested Tabs')
          if nested_tabs:
            index = 0
            removed = False
            while index < len(nested_tabs):
              # remove child index from the parent
              if not removed and child and nested_tabs[index] == tab_index - 1:
                nested_tabs.remove(tab_index - 1)
                removed = True
                index -= 1
              # decrement nested tab indexes by 1
              if nested_tabs[index] > tab_index - 1:
                nested_tabs[index] -= 1
              index += 1
        
        # remove child tab
        tabs.pop(key)
        print(f"\n-> Tab {key} closed successfully 👍")
        break
      else:
        print(f"\n-> Invalid index ({tab_index}) 🙂")
    except Exception as e:
      print("\n-> Something went wrong, please try again 🙂")
      print("Exception:", e, "\n")

# function: findLastOpenedTab
# params:
#   tabs: dictionary of tabs to search into
# description: find the greater index saved in the dictionary
def findLastOpenedTab(tabs):
  last_opened_tab = 0
  for key in tabs:
    if tabs.get(key).get("Tab Index") > last_opened_tab:
      last_opened_tab = tabs.get(key).get("Tab Index")
  return last_opened_tab + 1

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
      if not tab_index and tab_index != 0:
        tab_index = findLastOpenedTab(tabs)
      else:
        tab_index = int(tab_index)

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
            tabs[nested_tab_title] = {
              'Tab Index' : len(tabs),
              'URL': nested_tab_url
            }
            nested_tabs.append(len(tabs) - 1)
            print("\n-> Nested-Tab added successfully 👍\n")
            break
        else:
          print("\n-> You can not add a nested tab to a child tab 🙂")

        
      else:
        print(f"\n-> Invalid index ({parent_tab_index}) 🙂")
    except Exception as e:
      print("\n-> Something went wrong, please try again 🙂")
      print("Exception:", e, "\n")    

def sortTabs(tabs):
  print("\n***** Sorting all tabs based on their titles *****\n")

  if not tabs:
    print("\n-> There are no tabs to sort 🙂")
    return

  titles_list = list(tabs.keys())
  mergeSort(titles_list, 0, len(titles_list) - 1)

  new_dict = {}
  for i in range(len(titles_list)):
    if tabs.get(titles_list[i]).get('Nested Tabs') is not None:
      new_dict[titles_list[i]] = {
        'Tab Index' : tabs.get(titles_list[i]).get('Tab Index'),
        'URL': tabs.get(titles_list[i]).get('URL'),
        'Nested Tabs': tabs.get(titles_list[i]).get('Nested Tabs')
      }
    else:
      new_dict[titles_list[i]] = {
        'Tab Index' : tabs.get(titles_list[i]).get('Tab Index'),
        'URL': tabs.get(titles_list[i]).get('URL')
      }

  # update parent nested tabs indexes according with the new dictionary
  for key in new_dict:
    nested_tabs = new_dict.get(key).get('Nested Tabs')
    if nested_tabs:
      temp = []
      for i in range(len(nested_tabs)):
        temp.append(list(new_dict.keys()).index(list(tabs.keys())[nested_tabs[i]]))
      new_dict[key]['Nested Tabs'] = temp
      
  displayTabsIndexed(new_dict)
  print("\n-> Tabs sorted successfully 👍 \n")
  return new_dict
  
def mergeSort(list1,start,end):
  if start == end:
    return
  mid = (start + end) // 2
  mergeSort(list1, start, mid)
  mergeSort(list1, mid + 1, end)
  merge(list1, start, mid, end)

def merge(list1, start, mid, end):
  new_list = []
  ind1 = start
  ind2 = mid + 1

  while ind1 <= mid and ind2 <= end:
    if list1[ind1] < list1[ind2]:
      new_list.append(list1[ind1])
      ind1 += 1
    else:
      new_list.append(list1[ind2])
      ind2 += 1

  while ind1 <= mid:
    new_list.append(list1[ind1])
    ind1 += 1

  while ind2 <= end: 
    new_list.append(list1[ind2])
    ind2 += 1

  list1[start:end+1] = new_list

def saveTabs():
  print("bye 👋 bye 👋")
def importTabs():
  print("bye 👋 bye 👋")
def exit():
  print("bye 👋 bye 👋")

# only for testing purpose
def initializeTabsDictionary():
  tabs = {}
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
          'Nested Tabs': [5, 6, 7, 8, 9]
      },
      'Tab 2': {
          'URL': 'https://www.youtube.com',
          'Nested Tabs': [10, 11, 12, 13, 14]
      },
      'Tab 3': {
          'URL': 'https://www.facebook.com',
          'Nested Tabs': [15, 16, 17, 18, 19]
      },
      'Tab 4': {
          'URL': 'https://www.twitter.com',
          'Nested Tabs': [20, 21, 22, 23, 24]
      },
      'Tab 5': {
          'URL': 'https://www.instagram.com',
          'Nested Tabs': [25, 26, 27, 28, 29]
      },
      'Nested tab 1.1': {
          'URL': 'https://www.google.com/search?q=python'
      },
      'Nested tab 1.2': {
          'URL': 'https://www.google.com/search?q=java'
      },
      'Nested tab 1.3': {
          'URL': 'https://www.google.com/search?q=c++'
      },
      'Nested tab 1.4': {
          'URL': 'https://www.google.com/search?q=javascript'
      },
      'Nested tab 1.5': {
          'URL': 'https://www.google.com/search?q=php'
      },
      'Nested tab 2.1': {
          'URL': 'https://www.youtube.com/results?search_query=python'
      },
      'Nested tab 2.2': {
          'URL': 'https://www.youtube.com/results?search_query=java'
      },
      'Nested tab 2.3': {
          'URL': 'https://www.youtube.com/results?search_query=c++'
      },
      'Nested tab 2.4': {
          'URL': 'https://www.youtube.com/results?search_query=javascript'
      },
      'Nested tab 2.5': {
          'URL': 'https://www.youtube.com/results?search_query=php'
      },
      'Nested tab 3.1': {
          'URL': 'https://www.facebook.com/search?q=python'
      },
      'Nested tab 3.2': {
          'URL': 'https://www.facebook.com/search?q=java'
      },
      'Nested tab 3.3': {
          'URL': 'https://www.facebook.com/search?q=c++'
      },
      'Nested tab 3.4': {
          'URL': 'https://www.facebook.com/search?q=javascript'
      },
      'Nested tab 3.5': {
          'URL': 'https://www.facebook.com/search?q=php'
      },
      'Nested tab 4.1': {
          'URL': 'https://www.twitter.com/search?q=python'
      },
      'Nested tab 4.2': {
          'URL': 'https://www.twitter.com/search?q=java'
      },
      'Nested tab 4.3': {
          'URL': 'https://www.twitter.com/search?q=c++'
      },
      'Nested tab 4.4': {
          'URL': 'https://www.twitter.com/search?q=javascript'
      },
      'Nested tab 4.5': {
          'URL': 'https://www.twitter.com/search?q=php'
      },
      'Nested tab 5.1': {
          'URL': 'https://www.instagram.com/search?q=python'
      },
      'Nested tab 5.2': {
          'URL': 'https://www.instagram.com/search?q=java'
      },
      'Nested tab 5.3': {
          'URL': 'https://www.instagram.com/search?q=c++'
      },
      'Nested tab 5.4': {
          'URL': 'https://www.instagram.com/search?q=javascript'
      },
      'Nested tab 5.5': {
          'URL': 'https://www.instagram.com/search?q=php'
      },
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