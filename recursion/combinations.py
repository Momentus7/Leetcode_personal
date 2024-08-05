class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def func(start,res):
            if len(res)==k:
                resl.append(res)
            for o in range(start,n+1):
                func(o+1,res+[o])
        resl=[]
        func(1,[])
        return resl