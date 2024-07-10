def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the list from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", numbers)

bubble_sort(numbers)
print("Sorted list:", numbers)


################################################################

n = [13,32,26,35,10,98,23,2]

for i in range(len(n)-1):
    for j in range(len(n)-i-1):
        if n[j] > n[j+1]:
            swap = n[j]
            n[j] = n[j+1]
            n[j+1] = swap
        
print(n)