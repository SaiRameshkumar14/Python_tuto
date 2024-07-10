arr = [4,1,3,9,7]
n = len(arr)

for i in range(0,n-1):
    temp = i
    for j in range(i+1, n):
        if arr[j] < arr[temp]:
            temp = j
    arr[i], arr[temp] = arr[temp], arr[i]
    
print(arr)

# [1,3,4,7,9]