class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left,right=0,sum(nums)
        res=[-1]
        for i,ele in enumerate(nums):
            right-=ele
            if left==right:
                res[0]=i
                break
            left+=ele
        
        return res[0]