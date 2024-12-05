class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class bus(Vehicle):
    pass
ob1 = bus("School Volvo", 180, 12)
print(ob1.name)
print(ob1.max_speed)
print(ob1.mileage)