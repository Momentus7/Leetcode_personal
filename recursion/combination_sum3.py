class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def func(t,start,res,resl):
            if t<0:
                return
            if t==0 and len(res)==k:
                resl.append(res)
            
            for i in range(start,10):
                func(t-i,i+1,res+[i],resl)
        resl=[]
        func(n,1,[],resl)
        return resl