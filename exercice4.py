# Define a property that must have the same value for every class instance (object)
class Vehicle:
    # Class attribute
    color = "White"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    # def my_color(self, color):
    #     return f"Color : {color}, name: {self.name}, speed: {self.max_speed}, mileage: {self.mileage}"


# correction
class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


School_bus = Bus("School Volvo", 180, 12)
print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)
# my answer
# class Bus(Vehicle):
#     def my_color(self, color="white"):
#         return super(Bus, self).my_color(color="white")
#
#
# School_bus = Bus("School Volvo", 180, 12)
# print(School_bus.my_color())
#
#
# class Car(Vehicle):
#     def my_color(self, color="white"):
#         return super(Bus, self).my_color(color="white")
# School_bus = Bus("Audi Q5",240, 18)
# print(School_bus.my_color())
