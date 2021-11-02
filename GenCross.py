import numpy as np
import pandas as pd

def sort_letters(word):
    lr = word.replace('', ' ').strip().split(' ')
    lr.sort()
    return ''.join(lr)

def cross(col, ind):
    ls = []
    for i in col:
        nls = []
        for j in ind:
            nls.append(sort_letters(i + j))
        ls.append(nls)
    return pd.DataFrame(ls, columns=col, index=ind)

g1 = input('Genotype 1: ').replace(' ','').split(',')
g2 = input('Genotype 2: ').replace(' ','').split(',')
print(cross(g1, g2))
