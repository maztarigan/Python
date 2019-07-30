from module.student import Student  
from module.triangle import Triangle

s1 = Student()
print(s1.name)
print(s1.age)
print('\n')


s2 = Triangle(10,5)
print('Base is ',s2.base)
print('Hight is ',s2.hight)
print('Area is',s2.calculate_area())