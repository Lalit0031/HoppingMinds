# Bubble sort

arr = [10,2,13,32,23,24,14,53,21,41,1]
n = len(arr)
for i in range(n-1):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        
print(arr)