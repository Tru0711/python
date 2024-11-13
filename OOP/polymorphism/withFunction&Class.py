class Car:
    def start(self):
        return "Car started"

class Bike:
    def start(self):
        return "Bike started"

def start_vehicle(vehicle):
    print(vehicle.start())

car = Car()
bike = Bike()
start_vehicle(car)
start_vehicle(bike)
