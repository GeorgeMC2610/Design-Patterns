from Shape import Shape

class Rectangle(Shape):

    def __init__(self, width, height) -> None:
        
        self.width = width
        self.height = height

    def set_height(self, length):
        
        self.height = length

    def set_width(self, width):

        self.width = width

    def area(self):
        return self.width * self.height