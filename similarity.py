#!/usr/bin/python
# coding=utf-8
from math import sqrt
critics = {
    'Lisa': {
        'Lady in the water': 2.5,
        'Snake on a plane': 3.5
    },
    'Tom': {
        'Lady in the water': 3.0,
        'Snake on a plane': 4.0
    },
    'Jerry': {
        'Lady in the water': 2.0,
        'Snake on a plane': 3.0
    },
    'WXM': {
        'Lady in the water': 3.3,
        'Snake on a plane': 4.2
    },
    'jhz': {
        'Lady in the water': 3.9,
        'Snake on a plane': 4.5
    }
}

"""
欧几里得空间法 计算相似度
"""
def sim_distance(p1, p2):
    c = set(p1.keys()) & set(p2.keys())
    if not c:
        return 0
    sum_of_squares = sum([pow(p1.get(sk) - p2.get(sk), 2) for sk in c])
    p = 1 / (1 + sqrt(sum_of_squares))
    return p

"""
皮尔逊相关度
"""
def sim_distance_pearson(p1, p2):
    c = set(p1.keys()) & set(p2.keys())
    if not c:
        return 0
    s1 = sum([p1.get(sk) for sk in c])
    s2 = sum([p2.get(sk) for sk in c])
    sq1 = sum([pow(p1.get(sk), 2) for sk in c])
    sq2 = sum([pow(p2.get(sk), 2) for sk in c])
    ss = sum([p1.get(sk) * p2.get(sk) for sk in c])
    n = len(c)
    num = ss - s1 * s2 / n
    den = sqrt((sq1 - pow(s1, 2) / n) * (sq2 - pow(s2 - 2) / n))
    if den == 0:
        return 0
    p = num / den
    return p

"""
Jaccard系数
"""
def sim_distance_jaccard(p1, p2):
    c = set(p1.keys()) & set(p2.keys())
    if not c:
        return 0
    ss = sum([p1.get(sk) * p2.get(sk) for sk in c])
    sq1 = sum([pow(sk, 2) for sk in p1.values()])
    sq2 = sum([pow(sk, 2) for sk in p2.values()])
    p = float(ss) / (sq1 + sq2 - ss)
    return p

"""
余弦相似度
"""
def sim_distance_cos(p1, p2):
    c = set(p1.keys()) & set(p2.keys())
    if not c:
        return 0
    ss = sum([p1.get(sk) * p2.get(sk) for sk in c])
    sq1 = sqrt(sum([pow(p1.get(sk), 2) for sk in p1.values()]))
    sq2 = sqrt(sum([pow(p2.get(sk), 2) for sk in p2.values()]))
    p = float(ss) / (sq1 * sq2)
    return p

"""
得到top相似度高的前几位
"""
def topMatches(prefs, person, n=5, similarity=sim_distance_pearson):
    scores = [similarity(prefs, person, other)
              for other in prefs if other != person]
    scores.sort()
    scores.reverse()
    return scores[0:n]

"""
#利用所有他人评价值加权平均,为某人提供建议.
"""
def getRecommendations(prefs, person, similarity=sim_distance):
    totals = {}
    simSums = {}

    for other in prefs:
        if other == person:
            continue
        sim = similarity(prefs, person, other)
        # 忽略评价值为0或小于0的情况.
        if sim <= 0:
            continue
        for item in prefs[other]:
            # 只对自己还未曾看过的影片进行评价.
            if item not in prefs[person] or prefs[person][item] == 0:
                totals.setdefault(item, 0)
                totals[item] += sim * prefs[other][item]
                # 相似度之和
                simSums.setdefault(item, 0)
                simSums[item] += sim
        # 建立一个归一化的列表.
        rankings = [(total / simSums[item], item)
                    for item, total in totals.items()]
        rankings.sort()
        rankings.reverse()
        return rankings
