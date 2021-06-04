from itertools import combinations
s=input()
l=[''.join(p) for p in combinations(s,5)]
l.sort()
print(l)


