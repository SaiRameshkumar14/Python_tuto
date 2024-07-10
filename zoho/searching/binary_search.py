def binarysearch(arr,target):
    left = 0
    right = len(arr)
    
    while left <= right:
        mid = round((left+right) /2)
        
        if arr[mid] == target:
            return mid
            
        elif arr[mid] < target:
            left = mid +1
            
        else:
            right = mid-1
            
    return print("Target is not in array")
            
arr = [1, 2, 3, 4, 10, 12]
    
print(binarysearch(arr,7))