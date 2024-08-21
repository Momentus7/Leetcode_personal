class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=float('-inf')
        currsum=0

        for i in range(len(nums)):
            currsum+=nums[i]
            maxSum=max(currsum,maxSum)
            if currsum<0:
                currsum=0
        return maxSum