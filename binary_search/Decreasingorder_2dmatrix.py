class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=[0]
        def search(arr):
            left,right=0,len(arr)
            while left<right:
                mid=left+(-left+right)//2
                if arr[mid]>=0:
                    left=mid+1
                else:
                    right=mid
            return len(arr)-left
                    
        for i in grid:
            count.append(search(i))
        return sum(count)
        