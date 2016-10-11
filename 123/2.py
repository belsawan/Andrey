import random

a=-3
b=3
n=0
for i in range(10000000):
    c=random.uniform(a, b)
    if c >2 or c<-2: continue
    x=-c**2+4
    n=n+x
m=((b-a)/10000000)*(n)
print(m)


