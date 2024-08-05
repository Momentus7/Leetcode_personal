class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def func(ind,nums,res,resl):
            if len(nums)==ind:
                res.sort()
                if res not in resl:
                    resl.append(res)
            
            else:
                func(ind+1,nums,res+[nums[ind]],resl)
                func(ind+1,nums,res,resl)
        
        resl=[]
        func(0,nums,[],resl)
        return resl