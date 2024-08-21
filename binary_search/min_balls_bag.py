class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def func(maxballs):
            maxops=0
            for num in nums:
                ops=ceil(num/maxballs)-1
                maxops+=ops
            if maxops>maxOperations:
                return False
            else:
                return True
        left,right=1,max(nums)
        while left<=right:
            mid=left+(right-left)//2
            if func(mid):
                right=mid-1
            else:
                left=mid+1
        return left
