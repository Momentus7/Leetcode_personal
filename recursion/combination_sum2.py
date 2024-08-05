class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def func(t,nums,start,res,resl):
            if t<0:
                return
            res.sort()
            if t==0 and res not in resl:
                resl.append(res)
            
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                func(t-nums[i],nums,i+1,res+[nums[i]],resl)
        resl=[]
        func(target,candidates,0,[],resl)
        return resl