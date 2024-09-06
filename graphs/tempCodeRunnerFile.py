
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