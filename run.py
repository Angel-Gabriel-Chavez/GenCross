import numpy as np

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
    return np.array(ls)