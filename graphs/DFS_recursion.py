A=[[0,1],[1,2],[0,3],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]]

from collections import defaultdict

N= defaultdict(list)

#directed

for u,v in A:
    N[u].append(v)

def dfs_recursive(node):
    print(node)
    for nei_node in N[node]:
        if nei_node not in visited:
            visited.add(nei_node)
            dfs_recursive(nei_node)

visited=set()
source=0
visited.add(source)
dfs_recursive(source)


