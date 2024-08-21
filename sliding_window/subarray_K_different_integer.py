from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        res = 0
        distinct = defaultdict(int)
        l, m = 0, 0

        for r in range(len(nums)):
            distinct[nums[r]] += 1

            

            # invalid window
            while len(distinct) > k:
                
                distinct[nums[m]] -= 1
                if distinct[nums[m]] == 0:
                    del distinct[nums[m]]
                m += 1
                l = m

            # we have extra copies of a num
            while distinct[nums[m]] > 1:
                
                distinct[nums[m]] -= 1
                m += 1

            # valid window
            if len(distinct) == k:
                
                res += (m - l) + 1

        return res