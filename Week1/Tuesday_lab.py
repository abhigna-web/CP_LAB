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

#Sample Input  
#1 
#7  
#4 1 6 2 5 3 2 
#Expected Output 
#1 2 2 3 4 5 6


# Fractional Knapsack using Greedy Approach
t = int(input())
for _ in range(t):
    n, W = map(int, input().split()) 
    items = []
    for _ in range(n):
        v, w = map(int, input().split())
        items.append((v, w, v/w)) 
    # Sort items by value/weight ratio (descending)
    items.sort(key=lambda x: x[2], reverse=True)
    total_value = 0.0
    remaining_capacity = W
    for v, w, ratio in items:
        if remaining_capacity >= w:
            # take whole item
            total_value += v
            remaining_capacity -= w
        else:
            # take fraction of item
            total_value += ratio * remaining_capacity
            break
    print(f"{total_value:.6f}")

#Sample Input
#1
#3 50
#60 10
#100 20
#120 30
#Expected Output
#240.000000
