# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicel:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Buss(Vehicel):
     pass
b1= Vehicel("School volvo", 180, 12)
print("Name:",b1.name,"Speed:",b1.max_speed,"mileage:",b1.mileage)




