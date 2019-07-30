#Calculate the area of a triangle
class Triangle:
    def __init__(self, base, hight):
        self.base = base
        self.hight = hight

    def calculate_area(self):
        return self.base * self.hight /2