def create_int_arr():
    arr=[]
    while True:
        try:
            n=int(input("enter a number:"))
            arr.append(n)
        except Exception as e:
            return arr










def selection_sort_asc(arr):
    n=len(arr)
    for i in range(0,(n-1)):
        actualind=n-1-i
        max,currmaxind=-2147493648,-1
        for j in range(0,(n-i)):
            if max<arr[j]:
                max=arr[j]
                currmaxind=j
        arr[actualind],arr[currmaxind]=arr[currmaxind],arr[actualind]
arr=create_int_arr()
print("original array:",arr)
selection_sort_asc(arr)
print("selection sort asc:",arr)