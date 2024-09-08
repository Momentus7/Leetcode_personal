def quick_sort(arr):
    if len(arr)<=1:
        return arr
    
    p=arr[-1]
    
    L=[x for x in arr[:-1] if x<=p]
    R=[x for x in arr[:-1] if x>p]

    Left = quick_sort(L)
    Right= quick_sort(R)

    return Left+[p]+Right

arr=[-3,3,2,1,5,0]

print(quick_sort(arr))