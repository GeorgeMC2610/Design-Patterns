#SINGLE RESPONSIBILITY PRINCIPLE (SRP)

#This example shows how two different classes, do two different things.
#Both of those classes, only have one thing to do.

from animal_register import AnimalRegister
from animal_feed import AnimalFeed

print("Welcome to the zoo!")
animal = input("Type an animal to be registered in the zoo! --> ")
name = input(f"Give a name for the {animal}! --> ")

ar = AnimalRegister(name, animal)
ar.register()

af = AnimalFeed()
af.feed()
