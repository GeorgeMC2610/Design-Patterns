from Shape import Shape

class Square(Shape):

    def __init__(self, length) -> None:

        self.width = length
        self.height = length

    def set_width(self, length):

        self.width = length
        self.height = length

    def set_height(self, length):

        self.width = length
        self.height = length

    def area(self):

        return self.width * self.height