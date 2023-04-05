arr = [1,2,3,4,5,6,7,8,9,10]
n = len(arr)
for i in range(n-1):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        
x = int(input("Enter element to find : "))
low = 0
high = n-1
mid = 0
flag = 0

while low < high:
    mid = (low + high)//2
    if arr[mid] < x: low = mid+1
    elif arr[mid] > x: high = mid-1
    else:
        flag = 1
        print("item found at ",mid)
        break
    
if flag == 0:
    print("item not found!!") 
