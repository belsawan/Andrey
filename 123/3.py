import numpy as np
import random
import matplotlib.pyplot as plt
import pylab
values = [3, 4, 1, 2, 5, 6, 7, 8, 9, 10]
b=int(input())
def get_percentile(values,b):
    A=[0.0]
    for i in range(1, b):
         A.append(np.percentile(values, i*100/b))
    return A

percentiles=get_percentile(values,b)

def get_percentile_number(value, percentiles):
    i=0
    while percentiles[i]<= value:
        i+=1
        if i>=len(percentiles):
            i-=1
            return i
    return i-1
def value_equalization(value, percetiles, add_random):
    idx=get_percentile_number(value, percentiles)
    step=1/len(percentiles)
    if add_random==True:
        random_noise=random.uniform(0, step)
        new_value=idx*step + random_noise
    else:
        new_value=idx*step
    return new_value

def values_equalization(values, percentiles, add_random):
    for i in range(0, len(values)):
        values[i]=value_equalization(values[i], percentiles, add_random)
    return values
y = []
with open('img.txt', 'r') as f:
    for line in f:
        v = list(map(float, line.strip().split()))
        y.append(v)
data = np.array(y)

plt.subplot(221)
plt.imshow(data, cmap=plt.get_cmap('gray'))

plt.subplot(222)
val = [data.flatten()]
plt.hist(val, bins=10)

p = get_percentile(val, 3)

new_data = np.array(values_equalization(data.flatten(), p, add_random=True))
ready = new_data.reshape(200, 267)

data = np.array(y)

p = get_percentile(val, y)
new_data = np.array(values_equalization(data.flatten(), p, add_random=True))
ready = new_data.reshape(200, 267)

plt.subplot(223)
plt.imshow(ready, cmap=plt.get_cmap('gray'))
pylab.pause(1)

new_data = np.array(values_equalization(data.flatten(), p, add_random=True))
ready = new_data.reshape(200, 267)
plt.subplot(224)
data = [ready.flatten()]
plt.hist(data, bins=10)

plt.show()




















