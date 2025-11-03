def create_int_arr():
    arr=[]
    while True:
        try:
            n=int(input("enter a number:"))
            arr.append(n)
        except Exception as e:
            return arr

def selection_sortdesc(arr):
    n=len(arr)
    for i in range(0,n-1):
        actualind=n-1-i
        min=2**31
        currminind=-1
        for j in range(0,n-i):
            if min>arr[j]:
                min=arr[j]
                currminind=j
        arr[actualind],arr[currminind]=arr[currminind],arr[actualind]

arr=create_int_arr()
print("original array:",arr)
selection_sortdesc(arr)
print("the sorted array:",arr)