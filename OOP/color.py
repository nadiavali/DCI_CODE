class Vehicle:

    def __init__(self, name, max_speed, mileage, color ='white'):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color =color

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage,color='white'):
        super().__init__(name, max_speed, mileage,color='white')
    # def color(self, color='white'):
    #     return f'Color: {color}, Vehicle name: {self.name}, Speed:{self.max_speed}, Mileage:{self.mileage}'

# class Car(Vehicle):
#     def __init__(self, name, max_speed, mileage):
#         super().__init__(name, max_speed, mileage)
#     def color(self, color='white'):
#         return f'Color: {color}, Vehicle name: {self.name}, Speed:{self.max_speed}, Mileage:{self.mileage}'


School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity(25))