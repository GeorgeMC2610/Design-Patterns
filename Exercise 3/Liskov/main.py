### LISKOV SUBSTITUTION PRINCIPLE

from Shape import Shape
from Rectangle import Rectangle
from Square import Square

#here the program prints the area of a shape
def print_area(shape: Shape):

    print(f"Area of shape {shape.__class__.__name__} is {shape.area()}")

#but since Square are Rectangle are subtypes of Shape, it should work just fine.
print_area(Square(20))
print_area(Rectangle(15, 20))