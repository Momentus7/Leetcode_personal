def Insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
                
            else:
                break

A=[-4,-5,8,9,1,2,0,3]
Insertion_sort(A)
