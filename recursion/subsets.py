class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        resl=[]
        def func(ind,nums,res,resl):
            if ind==len(nums):
                resl.append(res)
            else:
                func(ind+1,nums,res+[nums[ind]],resl)
                func(ind+1,nums,res,resl)
            
        func(0,nums,[],resl)
        return resl      