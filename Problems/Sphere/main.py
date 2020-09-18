class Sphere:
    # finish class Sphere here
    PI = 3.1415

    def __init__(self, radius):
        self.radius = radius
        self.volume = 4 / 3 * self.PI * (radius ** 3)

class City:
    all_cities = []

    def __init__(self, name, year):
        self.name = name
        self.year = year

ny = City("New York", 1624)
ny.all_cities.append("New York")

stockholm = City("Stockholm", 1187)
stockholm.all_cities = ["Stockholm"]
print(City.all_cities)