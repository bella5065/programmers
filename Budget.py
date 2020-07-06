'''예산'''

'''
from itertools import combinations
def solution(d, budget):
    a = list()
    for i in range(len(d),0,-1):
        a.extend(map(list,combinations(d, i)))
    for j in range(len(a)):
        if budget >= sum(a[j]):
            return len(a[j])
'''

def solution(d, budget):
    d.sort()
    for i in range(len(d)):
        if sum(d) <= budget:
            return len(d)
        else:
            del d[-1]