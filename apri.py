#from __future__ import division
import pandas as pd
import numpy as np
from itertools import *
import math

its = []
ds = open('./16mcec17.csv','r').read().split('\n')
uni_its = []

for d in ds:
    it = d.split(',')
    for i in range(len(it)):
        it[i] = int(it[i])
    its.append(it)

itset = {}
for it in its:
    itset[it[0]] = it[1:]

for it in itset:
    for i in itset[it]:
        if i not in uni_its:
            uni_its.append(i)

uni_its.sort()

def find_support(it):

    c = 0
    for k in itset:
        f=0
        for i in it:
            if i not in itset[k]:
                f=1

        if f==0:
            c+=1

    return c

minimum_support = 2
cand_itset = []
pre_fre_itset = []

for iteration in range(1, len(uni_its)+1):

    print ("Step:" + str(iteration) + "\n")

    its = [list(i) for i in combinations(uni_its, iteration)]
    frequent_itemset = []

    for it in its:
        support = find_support(it)
        cand_itset.append([it, support])

    print (cand_itset)

    for it in cand_itset:
        if it[1]>=minimum_support:
            frequent_itemset.append(it)

    print (str(frequent_itemset) + "\n"+ str(len(frequent_itemset)))

    if len(frequent_itemset) == 0:
        pre_fre_itset = np.array(pre_fre_itset)
        print ("\nfrequent_itemset" + str(pre_fre_itset[:,0]))
        break

    cand_itset = []
    pre_fre_itset = frequent_itemset

