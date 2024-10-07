class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def func(i,j,area):
            dirr=[(0,1),(0,-1),(1,0),(-1,0)]

            for d in dirr:
                if -1<i+d[0]<len(grid) and -1<j+d[1]<len(grid[0]) and grid[i+d[0]][j+d[1]]==1:
                    grid[i+d[0]][j+d[1]]="#"
                    area[0]+=1
                    func(i+d[0],j+d[1],area)
            return
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    grid[i][j]="#"
                    area=[1]
                    func(i,j,area)
                    res=max(res,area[0])
        return res
        
