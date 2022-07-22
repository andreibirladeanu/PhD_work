from numpy import std, mean, sqrt
from itertools import combinations
def cohen_d(x,y):
    nx = len(x)
    ny = len(y)
    dof = nx + ny - 2
    return (mean(x) - mean(y)) / sqrt(((nx-1)*std(x, ddof=1) ** 2 + (ny-1)*std(y, ddof=1) ** 2) / dof)



    rad_abs_jitter = data[['localabsoluteJitter' ,'f0_mean']].loc[data['label'] == 'rad']
    norad_abs_jitter = data[['localabsoluteJitter','f0_mean']].loc[data['label'] == 'no_rad']

cohen_d(rad_abs_jitter['f0_mean'], norad_abs_jitter['f0_mean'])