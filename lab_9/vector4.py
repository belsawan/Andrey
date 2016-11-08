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

    def __sub__(self, other):
        return Vector(str(self.x-other.x)+' '+str(self.y-other.y))

n=int(input())
S=[]
for m in range(0, n):
    S.append(Vector(input()))
o=0
y=0
t=0
for i in range(len(S)):
    for j in range(len(S)):
        g=(S[i]-S[j]).module()
        if g>o:
            o=g
        if y<g<o:
            y=g
        if t<g<y:
            t=g
print(t+o+y)

