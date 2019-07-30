# The first class name must be UPPERCASE character
class Student:
    def __init__(self):
        self.name = 'Mazmur'
        self.age = 25

s1 = Student()
print(s1.name)
print(s1.age)
print('\n')


#Calculate the area of a triangle
class Triangle:
    def __init__(self, base, hight):
        self.base = base
        self.hight = hight

    def calculate_area(self):
        return self.base * self.hight /2


s2 = Triangle(10,5)
print('Base is ',s2.base)
print('Hight is ',s2.hight)
print('Area is',s2.calculate_area())