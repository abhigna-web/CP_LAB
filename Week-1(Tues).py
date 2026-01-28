# Merge Sort Program (Divide and Conquer)
def merge(arr, left, mid, right):
    # Copy the left half and right half into temporary lists
    L = arr[left:mid+1]   
    R = arr[mid+1:right+1] 
    i = j = 0 
    k = left  
    # Compare elements from L and R, and put the smaller one back into arr
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    # Copy any remaining elements from L
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    # Copy any remaining elements from R
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

# Function to apply merge sort
def merge_sort(arr, left, right):
    if left < right:  # base condition: at least 2 elements
        mid = (left + right) // 2  # find the middle point
        # Recursively sort the left half
        merge_sort(arr, left, mid)
        # Recursively sort the right half
        merge_sort(arr, mid + 1, right)
        # Merge the two sorted halves
        merge(arr, left, mid, right)
t = int(input()) 
for _ in range(t):
    n = int(input()) 
    arr = list(map(int, input().split()))
    merge_sort(arr, 0, n - 1)  # sort the array using merge sort
    print(" ".join(map(str, arr)))
