A=[[1,2],[2,3],[1,3],[0,1]]
n=4

M=[[0 for i in range(n)] for j in range(n) ]

#directed

for u,v in A:
    M[u][v]=1

