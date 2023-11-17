
cities = ["Tripoli", "Akkar", "Jbeil", "Saida", "Beirut"]
drivers = {}
drivers["driver1"] = ["Tripoli", "Akkar", "Jbeil", "Beirut", "Saida"]
drivers["driver2"] = ["Jbeil", "Beirut"]
drivers["driver3"] = ["Saida"]
# print(drivers.keys())
# print(drivers.values())
# print(drivers.items())

def displaySystemDrivers(drivers):
  print("\n***** Displaying system drivers *****\n")
  
  for i, key in enumerate(drivers, 1):
    print(f"{i}. {key}")

def displayDriversRoutes(drivers, driver = ""):
  print(f"\n***** Displaying {'<' + driver + '>' if driver else 'drivers'} routes *****\n")

  if driver:
    print(f"{driver} -> {drivers[driver]}") 
  else:
    for key in drivers:
      print(f"{key} -> {drivers[key]}")  

def displaySystemCities(cities):
  print("\n***** Displaying system cities *****\n")

  for i, elt in enumerate(cities, 1):
    print(f"{i}. {elt}")

def validateAddedCity(city, cities):
  valid = False
  max_length = 20

  if not city:
    print("-> City name cannot be empty. 🙃")
  elif not city.isalpha():
    print("-> City name should only contain alphabetic characters. 🙃")
  elif len(city) > max_length:
    print(f"-> City name should be at most {max_length} characters. 🙃")
  elif not city.istitle():
    print("-> City name should be in title case. (e.g. \"New York\") 🙃")
  elif city in cities:
    print("-> City name already exists. 🙃")
  else:
    valid = True

  return valid

def addCity(cities, drivers = {}, driver = ""):
    print(f"\n***** Adding a city {'to <' + driver + '>' if driver else ''} *****")

    while True:
      print("0️⃣  to return to main menu")
      city = input(f"\nEnter the city name{' you will visit ' if driver else ''}: ")
      
      city = city.strip()
      if city == "0":
        break
        
      valid = validateAddedCity(city, cities)
  
      if valid:
        cities.append(city)
        if driver:
          drivers[driver].append(city)
          displayDriversRoutes(drivers, driver)
        else:
          displaySystemCities(cities)
          break

def addDriver(drivers, cities):
  print("\n***** Adding a driver *****\n")
  
  driver = input("Enter the driver name: ")
  drivers[driver] = []
  displaySystemDrivers(drivers)
  addCity(cities, drivers, driver)
  
def addDriverCity(drivers, cities):
  print("\n***** Adding a driver city *****\n")
  
  driver = input("Enter the driver name: ")
  city = input("Enter the city name: ")
    
  if driver in drivers and city in cities:
    if city not in drivers[driver]:
      displayDriversRoutes(drivers, driver)

      while True:
        print("\nEnter")
        print(" 0. To add the city at the beginning of the route")
        print("-1. To add the city at the end of the route")
        print(" #. To add the city to the given index")

        try:
          choice = int(input("-> "))
    
          if choice == 0:
            drivers[driver].insert(choice, city)
          elif choice == -1:
            drivers[driver].append(city)
          else:
            if choice > 0:
              drivers[driver].insert(choice, city)
            else:
              print("\n-> Please enter a positive number 🙃")
              continue
          break
        except Exception as e:
          print("\n-> Please enter a valid number 🙃")
          print("Exception:", e, "\n")
      displayDriversRoutes(drivers, driver)
    else:
      print("-> City already exists. ")
  else:
    print("-> Driver/City name not found. 🙃")

def removeDriverCity(drivers):
  print("\n***** Removing a driver city *****\n")
  
  driver = input("Enter the driver name: ")
  city = input("Enter the city name: ")
  if driver in drivers and city in drivers[driver]:
    drivers[driver].remove(city)
    displayDriversRoutes(drivers, driver)
  else:
    print("-> Driver/City name not found. 🙃")

def checkDeliverability(drivers, cities):
  print("\n***** Checking deliverability *****\n")
  
  city = input("Enter the city name: ")
  if city not in cities:
    print("-> City name not found. 🙃")
  for driver in drivers:
    if city in drivers[driver]:
      print(f"-> {driver} is available")

def main(cities, drivers):
  while True:
    print("\n***** Main Menu *****\n")
    print("Enter")
    print("1️⃣  To add a city")
    print("2️⃣  To add a driver")
    print("3️⃣  To add a city to the route of a driver")
    print("4️⃣  Remove a city from a driver’s route")
    print("5️⃣  To check the deliverability of a package")
    print("6️⃣  To display the system drivers")
    print("7️⃣  To display the drivers' routes")
    print("8️⃣  To display the system cities")

    try:
      choice = int(input("-> "))
      if choice == 1:
        addCity(cities)
      elif choice == 2:
        addDriver(drivers, cities)
      elif choice == 3:
        addDriverCity(drivers, cities)
      elif choice == 4:
        removeDriverCity(drivers)
      elif choice == 5:
        checkDeliverability(drivers, cities)
      elif choice == 6:
        displaySystemDrivers(drivers)
      elif choice == 7:
        displayDriversRoutes(drivers)
      elif choice == 8:
        displaySystemCities(cities)
      else:
        print("\n-> Please enter a valid number 🙃")
    except Exception as e:
      print("\n-> Please enter a valid number 🙃")
      print("Exception:", e, "\n")

main(cities, drivers)







