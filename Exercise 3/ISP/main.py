### INTERFACE SEGREGATION PRINCIPLE
from car import Car
from truck import Truck
from aeroplane import Aeroplane

#the functionalities of the car, the truck and the aeroplane were separated in interfaces
car = Car()
truck = Truck()
aeroplane = Aeroplane()

#all three vehicles can move
car.move(10, 15)
truck.move(10, 10)
aeroplane.move(10, 15)

#all three can also be locked and unlocked
car.lock()
truck.lock()
aeroplane.lock()

car.unlock()
truck.unlock()
aeroplane.unlock()

#but only the Truck can attach to and detach from a trailer
truck.hook_trailer()
truck.detach_trailer()

#and the aeroplane is the only vehicle that can fly
aeroplane.fly(10, 15, 10)