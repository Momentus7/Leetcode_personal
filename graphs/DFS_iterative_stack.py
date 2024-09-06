A=[[0,1],[1,2],[0,3],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]]

from collections import defaultdict

N= defaultdict(list)

#directed

for u,v in A:
    N[u].append(v)

source=0
visited=set()
visited.add(source)
stack=[source]

while stack:
    node=stack.pop()
    print(node)

    for nei_node in N[node]:
        if nei_node not in visited:
            visited.add(nei_node)
            stack.append(nei_node)

