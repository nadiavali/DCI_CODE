class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    def type_bus(self):
        return type(self)

School_bus = Bus("School Volvo", 12, 50)
print(School_bus.type_bus())