left,curr,res=0,0,0

for i in range(len(nums)):
    curr+=nums[i]

    while curr>sum:
        left+=1
        curr-=nums[left]
    res=max(res,i-left+1)
return res
    
