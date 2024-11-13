class Vehicle:
    def start_engine(self):
        return "Engine started"

class Car(Vehicle):
    def drive(self):
        return "Driving car"

class Bike(Vehicle):
    def ride(self):
        return "Riding bike"

car = Car()
bike = Bike()
print(car.start_engine())
print(car.drive())
print(bike.start_engine())
print(bike.ride())
