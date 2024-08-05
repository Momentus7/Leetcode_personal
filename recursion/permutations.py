class Solution:
    
    def permute(self, nums: List[int]) -> List[List[int]]:

        def func(nums,res,resl):
            if not nums:
                resl.append(res)
            for i in range(len(nums)):
                func(nums[:i]+nums[i+1:],res+[nums[i]],resl)
        resl=[]
        func(nums,[],resl)
        return resl