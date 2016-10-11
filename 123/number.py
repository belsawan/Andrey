def values_equalization(values, percentiles, add_random=False):
    for i in range(0, len(values)):
        values[i]=value_equalization(values[i], percentiles, add_random=False)
    return values
print(values_equalization(values, percentiles, add_random=False)

def value_equalization(value, percetiles, add_random):
    idx=get_percentile_number(value, percentiles)
    step=1/len(percentiles)
    if add_random==True:
        random_noise=random.uniform(idx*step, (idx+1)*step)
        value=idx*step+random_noise
    else:
        value=idx*step
    return value
print(value_equalization(5.5, percentiles, add_random=True))

def value_equalization(value, percetiles, add_random):
    idx=get_percentile_number(value, percentiles)
    step=1/len(percentiles)
    if add_random==True:
        random_noise=random.uniform(idx*step, (idx+1)*step)
        new_value=idx*step + random_noise
    else:
        new_value=idx*step
    return new_value
print(value_equalization(5.5, percentiles))