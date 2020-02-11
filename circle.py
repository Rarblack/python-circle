import math


class Circle:
    radius = 0

    def __init__(self, radius):
        self.radius = radius

    def __calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def __calculate_area(self):
        return math.pi * self.radius * self.radius

    def print_perimeter(self):
        print('Radius: '+self.radius + ' => ' + 'Perimeter: ' + self.__calculate_perimeter())

    def print_area(self):
        print('Radius: '+self.radius + ' => ' + 'Area: ' + self.__calculate_area())
