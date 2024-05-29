class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):

        return self.width * self.height

    def calculate_perimeter(self):

        return 2 * (self.width + self.height)


rect = Rectangle(7, 11)
print(f"Площа прямокутника: {rect.calculate_area()}")
print(f"Периметр прямокутника: {rect.calculate_perimeter()}")