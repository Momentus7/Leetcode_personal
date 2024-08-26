class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # c={}
        # for i in nums:
        #     if i in c:
        #         c[i]+=1
        #     else:
        #         c[i]=1
        
        # for i in c:
        #     if c[i]>1:
        #         return i

        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]

            if slow==fast:
                break
        slow2=0

        while True:
            slow=nums[slow]
            slow2=nums[slow2]

            if slow==slow2:
                break
        return slow