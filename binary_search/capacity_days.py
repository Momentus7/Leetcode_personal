class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)

        while left<right:
            currwt,daysneed=0,1
            mid=left+(right-left)//2
            
            for weight in weights:
                
                if currwt+weight>mid:
                    daysneed+=1
                    currwt=0
                currwt+=weight
            if daysneed>days:
                left=mid+1
                
            else:
                right=mid

        return left
