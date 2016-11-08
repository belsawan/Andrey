import math

class Vector:
    def __init__(self, a='0 0'):
        self.x = float(a.split(' ')[0])
        self.y = float(a.split(' ')[1])
        self.name = 'Vector'

    def __add__(self, other):
        return Vector(str(self.x + other.x)+' '+str(self.y + other.y))

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __eq__(self, other):
        return self.x==other.x and self.y==other.y

    def __mul__(self, other):
        return Vector(str(self.x*other.x)+' '+str(self.y*other.y))

    def __str__(self):
        return self.name + ' CoorX = ' + str(self.x) + ' CoorY = ' + str(self.y)

    def module(self):
        return math.sqrt(self.x**2+self.y**2)

    def __truediv__(self, r):
        return Vector(str(self.x/r)+' '+str(self.y/r))

n=int(input())
S=[]
for m in range(0, n):
    S.append(Vector(input()))
g=0
for i in range(len(S)):
    o=S[i].module()
    if o>g:
        g=o
for p in range(len(S)):
    if S[p].module()==g:
        print(S[p])




