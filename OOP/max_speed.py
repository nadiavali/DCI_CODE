class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name =name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)
        pass



    # def max_speed(self):
    #     return self.max_speed

    # def mileage(self):
    #     return self.mileage

# class Vehicle(): #without variables and methods
#     pass


# v = Vehicle(60, 23)
# print(v.max_speed)
# print(v.mileage)
#print(v)

b = Bus('Volvo', 70, 4)
print('vehicle Name:', b.name, 'speed:', b.max_speed, 'mileage:', b.mileage)