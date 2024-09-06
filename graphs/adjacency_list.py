A=[[1,2],[2,3],[1,3],[0,1],[3,0]]

from collections import defaultdict

N= defaultdict(list)

#directed

for u,v in A:
    N[u].append(v)

print(N)