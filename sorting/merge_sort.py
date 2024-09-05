def merge_sort(arr):
    if len(arr)==1:
        return arr
    m=len(arr)//2

    sorted_left=merge_sort(arr[:m])
    sorted_right=merge_sort(arr[m:])

    return merge(sorted_left,sorted_right)
def merge(left,right):
    
    i,j=0,0
    res=[]

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    
    res.extend(left[i:])
    res.extend(right[j:])
    return res

A=[-4,-5,8,9,1,2,0,3]

A=merge_sort(A)

print(A)





