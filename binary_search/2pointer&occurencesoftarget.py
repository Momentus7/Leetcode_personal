class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left,right=0,len(nums)-1
        

        while left<=right:

            mid=left+(right-left)//2

            if nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                first,last=mid,mid
                while first > 0 and nums[first]==nums[first-1]:
                    first-=1
                while last < len(nums)-1 and nums[last]==nums[last+1]:
                    last+=1
                return [first,last]
                
                
        return [-1,-1]
