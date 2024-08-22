class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand=0
        count=0
        for i in nums:
            if count==0:
                cand=i
            if cand==i:
                count+=1
            else:
                count-=1
        return cand