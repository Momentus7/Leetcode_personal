class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left,num_zeroes=0,0
        res=0

        for i in range(len(nums)):
            if nums[i]==0:
                num_zeroes+=1

            while num_zeroes>k:
                if nums[left]==0:
                    num_zeroes-=1
                left+=1
            res=max(res,i-left+1)
        return res