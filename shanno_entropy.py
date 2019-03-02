#!/usr/bin/python2.7
# -*-encoding:utf8 -*-
from __future__ import division

import math
log2 = lambda x: math.log(x, 2)

def get_shanno_entropy(values):
    ''' 根据给定列表中的值计算其Shanno Entropy
    '''
    uniq_vals = set(values)
    val_nums = {key: values.count(key) for key in uniq_vals}
    probs = [v/len(values) for k, v in val_nums.items()]
    entropy = sum([-prob*log2(prob) for prob in probs])
    return entropy




values = [2,2,3,3,3,3,4,4,4,5]
print get_shanno_entropy(values)