class Solution():
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        if sum(nums)%k:
            return False
        nums.sort(reverse=True)

        target=sum(nums)//k
        used=[False]*len(nums)
        
        def func(ind,k,subsetsum):
            if k==0:
                return True
            if subsetsum==target:
                return func(0,k-1,0)
            for i in range(ind,len(nums)):
                if used[i] or subsetsum+nums[i]>target:
                    continue
                if (i>0 and nums[i]==nums[i-1] and not used[i-1]):
                    continue
                used[i]=True
                if func(i+1,k,subsetsum+nums[i]):
                    return True
                used[i]=False
            return False
        return func(0,k,0)