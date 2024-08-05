class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def func(t,nums,start,res,resl):

            res.sort()

            if t<0:
                return

            if t==0 and res not in resl:
                resl.append(res)

            for i in range(start,len(nums)):
                func(t-nums[i],nums,i,res+[nums[i]],resl)
        
        resl=[]
        func(target,candidates,0,[],resl)
        return resl