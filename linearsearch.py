def create_int_arr():
    arr=[]
    while True:
        try:
            n=int(input("enter a number:"))
            arr.append(n)
        except Exception as e:
            return arr






def linear_search(arr,target):
    flag,index=False,-1
    for i in range(0,len(arr)):
        if target==arr[i]:
            flag=True
            index=i
    return flag,index
arr=create_int_arr()
target=int(input("enter the element to be search"))
fla,ind=linear_search(arr,target)
print(fla)
print(ind)
print("sucessfully executed")

