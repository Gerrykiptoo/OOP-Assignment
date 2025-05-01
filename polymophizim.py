class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        pass  # Abstract method

class Car(Vehicle):
    def move(self):
        print(f"{self.brand} is driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print(f"{self.brand} is flying through the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print(f"{self.brand} is sailing on water ⛵")

# Create objects
vehicles = [
    Car("Toyota"),
    Plane("Boeing"),
    Boat("Viking Cruises")
]

for vehicle in vehicles:
    vehicle.move()

