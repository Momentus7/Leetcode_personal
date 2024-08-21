class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        max_window=0
        left=0
        window=0
        base=0

        for r in range(len(customers)):

            if grumpy[r]:
                window+=customers[r]
            else:
                base+=customers[r]
            
            while r-left+1>minutes:#if also works..since fixed wondow of 3 and we reduce by one
                if grumpy[left]:
                    window-=customers[left]
                left+=1
            
            max_window=max(max_window,window)

        return max_window+base