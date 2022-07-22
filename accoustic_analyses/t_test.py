from numpy import std, mean, sqrt
from itertools import combinations
from scipy.stats import ttest_ind


def t_test(data, column)

grps = data['label'].unique()
combs = combinations(grps, 2)

ttests = {
    f'{c1}_{c2}': ttest_ind(
        data.loc[data['label'] == c1, column], 
        data.loc[data['label'] == c2, column]
    ) for c1, c2 in combs
}




data.groupby('label')[column].mean()