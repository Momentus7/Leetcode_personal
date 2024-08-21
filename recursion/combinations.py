class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def func(start,res):
            if len(res)==k:
                resl.append(res)
            for i in range(start,n+1):
                func(i+1,res+[i])
        resl=[]
        func(1,[])
        return resl