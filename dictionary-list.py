dealership = {
  "cars": [
    {
      "brand": "Honda",
      "year": 2023,
      "speed": 999
    },
    {
      "brand": "Honda",
      "year": 2020,
      "speed": 150
    },
    {
      "brand": "Toyota",
      "year": 2023,
      "speed": 250
    },
    {
      "brand": "Toyota",
      "year": 1980,
      "speed": 200
    },
    {
      "brand": "Toyota",
      "year": 2025,
      "speed": 300
    },
    {
      "brand": "Mustang",
      "year": 1990,
      "speed": 140
    },
    {
      "brand": "Mustang",
      "year": 2020,
      "speed": 500
    }
  ],
  "trucks": [
    {
      "name": "Mr. Sexy",
      "type": "4x4",
      "experience": "used"
    },
    {
      "name": "Ms. Worldwide",
      "type": "8x8",
      "experience": "new"
    }
  ]
}

#extra

# find the 3 oldest cars
cars = dealership["cars"]
def get_year(car):
    return car["year"]
sorted_cars = sorted(cars, key=get_year)
oldest_cars = sorted_cars[:3]
user = input("Press enter to get a list of the 3 oldest cars.")
for car in oldest_cars:
    print("Brand:", car["brand"])
    print("Year:", car["year"])
    print("Speed:", car["speed"])
    print()

# give me a list of all toyotas older than 2020
cars = dealership["cars"]
older_toyotas = []
for car in cars:
    if car["brand"].lower() == 'toyota' and car["year"] > 2020:
        older_toyotas.append(car)
user = input("Press enter to get a list of Toyota cars older than 2020.")
for car in older_toyotas:
    print("Brand:", car["brand"])
    print("Year:", car["year"])
    print("Speed:", car["speed"])
    print()

# give me a list of the fastest cars above 300
cars = dealership["cars"]
fastest_cars = []
for car in cars:
    if car["speed"] > 300:
        fastest_cars.append(car)
user = input("Press enter get a list of cars with speed above 300.")
for car in fastest_cars:
    print("Brand:", car['brand'])
    print("Year:", car["year"])
    print("Speed:", car["speed"])
    print()


#1.find the "newest" car
cars = dealership["cars"]
newest_car = 0
car_brand = None
user = input("Press enter to find the newest car:\n")
for car in cars:
    if car['year'] > newest_car:
        newest_car = car["year"]
        car_brand = car["brand"]
print(f"The {car_brand} from the year {newest_car}.\n")

#2. find the "fastest" car
cars = dealership["cars"]
fastest_car = 0
car_brand = None
user = input("Press enter to find the fastest car:\n")
for car in cars:
    if car["speed"] > fastest_car:
        fastest_car = car["speed"]
        car_brand = car["brand"]
print(f"The {car_brand} with a speed of {fastest_car}km/hr.\n")


#3.find a car brand "toyota" and give me all the information
cars = dealership["cars"]
toyota_info = None
user = input("Press enter to find info of Toyota car:\n")
for car in cars:
    if car["brand"].lower() == "toyota":
        toyota_info = car
        break
if toyota_info is not None:
    print("Toyota's information: \n")
    for key, value in toyota_info.items():
        print(f"{key}:{value}")
else:
    print("No Toyota found.")


#4.Which is the "4x4" truck?
trucks = dealership["trucks"]
four_by_four = None
user = input("Press enter to find the 4x4 truck:\n")
for truck in trucks:
    if truck["type"] == "4x4":
        four_by_four = truck["name"]
print(f"The 4x4 car is called {four_by_four}.\n")

#5.which truck is "new"?
trucks = dealership["trucks"]
new_truck = None
user = input("Press enter to find the newest truck:\n")
for truck in trucks:
    if truck["experience"] == "new":
        new_truck = truck["name"]
print(f"The new truck is called {new_truck}.\n")