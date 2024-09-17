class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        arr=sorted(intervals, key=lambda x:x[0])
        res=[]

        for x in arr:
            if not res or res[-1][1]<x[0]:
                res.append(x)
            else:
                res[-1][1]=max(res[-1][1],x[1])
        return res