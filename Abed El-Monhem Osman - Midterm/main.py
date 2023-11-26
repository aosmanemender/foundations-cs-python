import requests
from bs4 import BeautifulSoup
import json

# function: greetingUser
# description: displaying user greeting
# time complexity: O(1)
def greetingUser():
  print("\n***** Hello, And Welcome *****\n")


# function: displayMenu
# description: displaying the main menu with a variety of options
# time complexity: O(1)
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
# time complexity: O(m * n)
def openTab(tabs):
  print("\n***** Opening a new tab *****")

  while True:      #O(m), m being the number of times the user inputs invalid title/url
    tab_title = input("\nEnter the tab title: ")
    tab_url = input("Enter the tab URL: ")

    if validateAddedTab(tab_title, tab_url):
      tabs[tab_title] = {
        'Tab Index' : len(tabs) if tabs else 0,
        'URL': tab_url,
        'Nested Tabs': []
      }
      print("\n-> Tab added successfully 👍\n")
      displayTabsIndexed(tabs)      #O(n), n being the length of the dict
      break


# function: validateAddedTab
# params:
#   tab_title: title entered by the user
#   tab_url: url address entered by the user
# return: True/False
# description: validating user inputs (tab title, tab url) before adding it to the tabs dict
# time complexity: O(1)
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
# time complexity: O(n), n being the length of the dict
def displayTabsIndexed(tabs):
  for i, key in enumerate(tabs, 1):      #O(n)
    print(f"{i}. {key} -> {tabs.get(key).get('URL')}")


# function: displayParentTabsIndexed
# params:
#   tabs: dictionary of tabs to be printed
# description: displaying only parent tabs with index number to be picked by the user
# time complexity: O(n), n being the length of the dict
def displayParentTabsIndexed(tabs):
  for i, key in enumerate(tabs, 1):      #O(n)
    nested_tabs = tabs.get(key).get('Nested Tabs')
    if nested_tabs is not None:
      print(f"{i}. {key} -> {tabs.get(key).get('URL')}")


# function: closeTab
# params:
#   tabs: dictionary of tabs to be updated
# description: removing a tab from the tabs dict
# time complexity: O(m*(n + n + n*(n*k)))) = O(m(2n + kn^2)))) = O(mkn^2), m being the number of times the user inputs invalid tab index, k being the number of nested tabs, n being the length of the dict
def closeTab(tabs):
  print("\n***** Closing a tab *****")

  if not tabs:
    print("\n-> There are no tabs to close 🙂")
    return

  while True:      #O(m), m being the number of times the user inputs invalid index
    try:
      print("\nEnter the index of the tab you wish to close: \n")
      displayTabsIndexed(tabs)          #O(n), n being the length of the dict

      tab_index = input("-> ")
      if not tab_index and tab_index != 0:
        tab_index = findLastOpenedTab(tabs)         #O(n), n being the length of the dict
      else:
        tab_index = int(tab_index)

      if tab_index in range(1, len(tabs) + 1):      #O(n), n being the length of the dict
        key = list(tabs.keys())[tab_index - 1]
        child = tabs.get(key).get('Nested Tabs') is None

        # decrement tab indexes by 1
        for tab in tabs:                            #O(n), n being the length of the dict
          if tabs[tab]['Tab Index'] > tab_index - 1:
            tabs[tab]['Tab Index'] -= 1
          nested_tabs = tabs.get(tab).get('Nested Tabs')
          if nested_tabs:
            index = 0
            removed = False
            while index < len(nested_tabs):         #O(k), k being the length of nested tabs
              # decrement nested tab indexes by 1
              if nested_tabs[index] > tab_index - 1:
                nested_tabs[index] -= 1
                
              # remove child index from the parent
              if not removed and child and nested_tabs[index] == tab_index - 1:
                nested_tabs.remove(tab_index - 1)
                removed = True
                index -= 1
              
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
# time complexity: O(n), n being the length of the dict
def findLastOpenedTab(tabs):
  last_opened_tab = 0
  for key in tabs:          #O(n), n being the length of the dict
    if tabs.get(key).get("Tab Index") > last_opened_tab:
      last_opened_tab = tabs.get(key).get("Tab Index")
  return last_opened_tab + 1


# function: swicthTab
# params:
#   tabs: dictionary of tabs to be searched into
# description: printing HTML content of the switched tab
# time complexity: O(m(n + n + n)) = O(m*n), n being the length of the dict, m being the number of times the user inputs invalid index
# online reference: https://realpython.com/beautiful-soup-web-scraper-python/
def swicthTab(tabs):
  print("\n***** Switching to a tab *****")

  if not tabs:
    print("\n-> There are no tabs to switch to 🙂")
    return

  while True:      #O(m), m being the number of times the user inputs invalid index
    try:
      print("\nEnter the index of the tab you wish to switch to: \n")
      displayTabsIndexed(tabs)          #O(n), n being the length of the dict

      tab_index = input("-> ")
      if not tab_index and tab_index != 0:
        tab_index = findLastOpenedTab(tabs)         #O(n), n being the length of the dict
      else:
        tab_index = int(tab_index)

      if tab_index in range(1, len(tabs) + 1):         #O(n), n being the length of the dict
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
# time complexity: O(n*m + n*n*m) = O(mn^2), n being the length of the dict, m being the length of nested tabs
def displayTabs(tabs):
  print("\n***** Displaying all tabs *****\n")

  if not tabs:
    print("-> There are no tabs to display 🙂")
    return

  for key in tabs:      #O(n), n being the length of the dict
    nested_tabs = tabs.get(key).get('Nested Tabs')
    if nested_tabs is not None:
      print(f"{key} -> {tabs.get(key).get('URL')}")
      for nt in nested_tabs:      #O(m), m being the length of nested tabs
        print("\t", list(tabs.keys())[nt], "->", tabs.get(list(tabs.keys())[nt]).get('URL'))
    else:
      # display the children if the parent is dead
      # parent is dead when the child index is not found in the nested tabs indexes
      parent_dead = True
      for key2 in tabs:      #O(n), n being the length of the dict
        child_index = list(tabs.keys()).index(key)
        nested_tabs = tabs.get(key2).get('Nested Tabs')
        if nested_tabs and child_index in nested_tabs:      #O(m), m being the length of nested tabs
          parent_dead = False
      if parent_dead:
        print(f"{key} -> {tabs.get(key).get('URL')}")

# function: openNestedTab
# params:
#   tabs: dictionary of tabs to be updated
# description: adding a new nested tab to tabs dictionary
# time complexity: O(m (n + n * 1)), n being the length of the list, m being the number of times the user enters invalid index  -> O(m * n)
def openNestedTab(tabs):
  print("\n***** Opening nested tab *****")

  if not tabs:
    print("\n-> There are no tabs to create nested tabs from 🙂")
    return

  while True:      # O(m)
    try:
      print("\nEnter the index of the parent tab where you want to insert additional tabs: \n")
      displayParentTabsIndexed(tabs)      # O(n)

      parent_tab_index = int(input("-> "))

      if parent_tab_index in range(1, len(tabs) + 1):      # O(n)
        nested_tabs = tabs.get(list(tabs.keys())[parent_tab_index - 1]).get('Nested Tabs')
        if nested_tabs is not None:
          nested_tab_title = input("\nEnter the nested tab title: ")
          nested_tab_url = input("Enter the nested tab URL: ")

          if validateAddedTab(nested_tab_title, nested_tab_url):      # O(1)
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


# function: sortTabs
# params:
#   tabs: dictionary of tabs to be sorted
# return:
#   new_dict: the new sorted dictionary 
# description: sorting tabs using merge-sort based on their titles
# time complexity: O(n log n + n + n*m + n), n being the number of tabs, m being the number of nested tabs, O(nlogn) dominates the other terms -> O(nlogn)
def sortTabs(tabs):
  print("\n***** Sorting all tabs based on their titles *****\n")

  if not tabs:
    print("-> There are no tabs to sort 🙂")
    return

  titles_list = list(tabs.keys())
  mergeSort(titles_list, 0, len(titles_list) - 1)      # O(n log n)

  new_dict = {}
  for i in range(len(titles_list)):      # O(n)
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
  for key in new_dict:      # O(n)
    nested_tabs = new_dict.get(key).get('Nested Tabs')
    if nested_tabs:
      temp = []
      for i in range(len(nested_tabs)):      # O(m)
        temp.append(list(new_dict.keys()).index(list(tabs.keys())[nested_tabs[i]]))

      new_dict[key]['Nested Tabs'] = temp

  displayTabsIndexed(new_dict)      # O(n)
  print("\n-> Tabs sorted successfully 👍 \n")
  return new_dict


# function: mergeSort
# params:
#   list1: list of titles to be sorted
#   start: the start index of the list
#   end: the end index of the list
# description: it divides the list, and then calls the merge function
# time complexity: O(n log n), n being the length of the list
def mergeSort(list1,start,end):
  if start == end:
    return
  mid = (start + end) // 2
  mergeSort(list1, start, mid)
  mergeSort(list1, mid + 1, end)
  merge(list1, start, mid, end)


# function: merge
# params:
#   list1: list of titles to be sorted
#   start: the start index of the list
#   mid: the middle index of the list
#   end: the end index of the list
# description: it merges the two sublists into a sorted one
# time complexity: O(n), n being the length of the list
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


# function: saveTabs
# params:
#   tabs: dictionary of tabs to be saved
# description: save all tabs to an external file
# time complexity: O(n), n being the length of the dict
# online reference: https://www.javatpoint.com/save-json-file-in-python
def saveTabs(tabs):
  print("\n***** Saving tabs to an external file *****")

  if not tabs:
    print("\n-> There are no tabs to save 🙂")
    return

  print("\nEnter the file path where you want to save the current state of tabs: \n")
  file_path = input("-> ")
  print("\nIt may takes time. Please wait . . .\n")

  try:
    saveTabsCurrentState(file_path, tabs)          #O(n), n being the length of tabs
  except Exception as e:
    print("\n-> Something went wrong, please try again 🙂")
    print("Exception:", e, "\n")


# function: saveTabsCurrentState
# params:
#   file_path: location of the file where the tabs should be saved
#   tabs: dictionary of tabs to be saved
# description: save all tabs to an external file
# time complexity: O(n), n being the length of tabs
def saveTabsCurrentState(file_path, tabs):
  Json_value = {}
  for key in tabs:          #O(n), n being the length of tabs
    URL = tabs.get(key).get('URL')
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    child = tabs.get(key).get('Nested Tabs') is None
    if not child:
      Json_value[key] = {
        "Tab Index": tabs.get(key).get('Tab Index'),
        "URL": URL,
        "Content": str(soup),
        "Nested Tabs": tabs.get(key).get('Nested Tabs')
      }
    else:
      Json_value[key] = {
        "Tab Index": tabs.get(key).get('Tab Index'),
        "URL": URL,
        "Content": str(soup)
      }

  save_file = open(file_path + ".json", "w")  
  json.dump(Json_value, save_file, indent = 4)          #O(n), n being the size of json
  save_file.close()
  print("-> Tabs saved successfully 👍\n")


# function: importTabs
# description: importing data from the user file
# time complexity: O(n), n being the size of JSON data
def importTabs():
  print("\n***** Importing tabs from an external file *****")

  print("\nEnter the file path in order to load tabs from: \n")
  file_path = input("-> ")

  try:
    tabs = loadTabs(file_path)          #O(n), n being the size of JSON data
    return tabs
  except Exception as e:
    print("\n-> Something went wrong, please try again 🙂")
    print("Exception:", e, "\n")


# function: loadTabs
# params:
#   file_path: location of the file where the data should be loaded from
# description: loading all tabs saved in the file into the system
# time complexity: O(n), n being the size of JSON data
def loadTabs(file_path):
  try:
    load_file = open(file_path + ".json", "r")
    tabs = json.load(load_file)

    new_dict = {}
    for key in tabs:
      child = tabs.get(key).get('Nested Tabs') is None
      if not child:
        new_dict[key] = {
          'Tab Index' : tabs.get(key).get('Tab Index'),
          'URL': tabs.get(key).get('URL'),
          'Nested Tabs': tabs.get(key).get('Nested Tabs')
        }
      else:
        new_dict[key] = {
          'Tab Index' : tabs.get(key).get('Tab Index'),
          'URL': tabs.get(key).get('URL')
        }
    load_file.close()
    print("\n-> Tabs loaded successfully 👍\n")
    
    return new_dict
  except Exception as e:
    print("\n-> Something went wrong, please try again ")
    print("Exception:", e, "\n")

# function: exit
# description: exit the program
# time complexity: O(1)
def exit():
  print("\n-> bye 👋 bye 👋")


# only for testing purpose
def initializeTabsDictionary():
  tabs = {}
  tabs = {
      'Tab 1': 'https://www.google.com',
      'Tab 2': 'https://www.youtube.com',
      'Tab 3': 'https://www.facebook.com',
      'Tab 4': 'https://www.twitter.com',
      'Tab 5': 'https://www.linkedin.com'
  }
  tabs = {
      'Tab 1': {
          'Tab Index' : 0,
          'URL': 'https://www.google.com',
          'Nested Tabs': [3, 4, 5, 6, 7]
      },
      'Tab 2': {
          'Tab Index' : 1,
          'URL': 'https://www.youtube.com',
          'Nested Tabs': [8, 9, 10, 11, 12]
      },
      'Tab 3': {
          'Tab Index' : 2,
          'URL': 'https://www.facebook.com',
          'Nested Tabs': [13, 14, 15, 16, 17]
      },
      'Nested tab 1.1': {
          'Tab Index' : 3,
          'URL': 'https://www.google.com/search?q=python'
      },
      'Nested tab 1.2': {
          'Tab Index' : 4,
          'URL': 'https://www.google.com/search?q=java'
      },
      'Nested tab 1.3': {
          'Tab Index' : 5,
          'URL': 'https://www.google.com/search?q=c++'
      },
      'Nested tab 1.4': {
          'Tab Index' : 6,
          'URL': 'https://www.google.com/search?q=javascript'
      },
      'Nested tab 1.5': {
          'Tab Index' : 7,
          'URL': 'https://www.google.com/search?q=php'
      },
      'Nested tab 2.1': {
          'Tab Index' : 8,
          'URL': 'https://www.youtube.com/results?search_query=python'
      },
      'Nested tab 2.2': {
          'Tab Index' : 9,
          'URL': 'https://www.youtube.com/results?search_query=java'
      },
      'Nested tab 2.3': {
          'Tab Index' : 10,
          'URL': 'https://www.youtube.com/results?search_query=c++'
      },
      'Nested tab 2.4': {
          'Tab Index' : 11,
          'URL': 'https://www.youtube.com/results?search_query=javascript'
      },
      'Nested tab 2.5': {
          'Tab Index' : 12,
          'URL': 'https://www.youtube.com/results?search_query=php'
      },
      'Nested tab 3.1': {
          'Tab Index' : 13,
          'URL': 'https://www.facebook.com/search?q=python'
      },
      'Nested tab 3.2': {
          'Tab Index' : 14,
          'URL': 'https://www.facebook.com/search?q=java'
      },
      'Nested tab 3.3': {
          'Tab Index' : 15,
          'URL': 'https://www.facebook.com/search?q=c++'
      },
      'Nested tab 3.4': {
          'Tab Index' : 16,
          'URL': 'https://www.facebook.com/search?q=javascript'
      },
      'Nested tab 3.5': {
          'Tab Index' : 17,
          'URL': 'https://www.facebook.com/search?q=php'
      },
  }

  return tabs


def menu():
  # tabs = initializeTabsDictionary()
  tabs = {}
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
        swicthTab(tabs)
      elif choice == 4:
        displayTabs(tabs)
      elif choice == 5:
        openNestedTab(tabs)
      elif choice == 6:
        tabs = sortTabs(tabs)
      elif choice == 7:
        saveTabs(tabs)
      elif choice == 8:
        tabs = importTabs()
      elif choice == 9:
        exit()
        break
      else:
        print("\n-> Please enter a valid number 🙂")
    except Exception as e:
      print("\n-> Something went wrong, please try again 🙂")
      print("Exception:", e, "\n")


menu()
