import random

a=-3
b=3
n=0
for i in range(1000000):
    c=random.uniform(a, b)
    x=-c**2+4
    n=n+x
m=((b-a)/1000000)*(n)
print(m)


