import math

class Vector:
    def __init__(self, a='0 0'):
        self.x = a.split(' ')[0]
        self.y = a.split(' ')[1]
        self.name='Vector'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __eq__(self, other):
        return self.x==other.x and self.y==other.y

    def __mul__(self, other):
        return Vector(self.x*other.x, self.y*other.y)

    def __str__(self):
        return self.name + ' CoorX = ' + str(self.x) + ' CoorY = ' + str(self.y)

    def module(self):
        return math.sqrt(self.x**2+self.y**2)


a=list(map(int, input().split()))
b=list(map(int, input().split()))
A=Vector(a[0],a[1])
B=Vector(b[0],b[1])
print(A.module())





