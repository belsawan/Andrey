import numpy as np

values = [3, 4, 1, 2, 5, 6, 7, 8, 9, 10]
def get_percentile(values,b):
    for i in range(b, 0, -1):
        if i==0:
            p=0
        else:
            p=100/i
        if p!=100:
            print(np.percentile(values,p))

get_percentile(values, int(input()))





