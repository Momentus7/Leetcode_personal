def bubble_sort(arr):
    n=len(arr)
    flag=True
    while flag:
        flag=False
        for i in range(1,n):
            if arr[i-1]>arr[i]:
                flag=True
                arr[i-1],arr[i]=arr[i],arr[i-1]
                print(A)

A=[-4,-5,8,9,1,2,0,3]
bubble_sort(A)
