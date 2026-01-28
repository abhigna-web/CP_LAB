def max_crossing_sum(arr, left, mid, right):
    # Include elements on left of mid
    total = 0
    left_sum = -10**18
    for i in range(mid, left - 1, -1):
        total += arr[i]
        left_sum = max(left_sum, total)
    # Include elements on right of mid
    total = 0
    right_sum = -10**18
    for i in range(mid + 1, right + 1):
        total += arr[i]
        right_sum = max(right_sum, total)
    return left_sum + right_sum

def max_subarray_sum(arr, left, right):
    # Base case: only one element
    if left == right:
        return arr[left]
    mid = (left + right) // 2
    # Maximum subarray sum in left half
    left_max = max_subarray_sum(arr, left, mid)
    # Maximum subarray sum in right half
    right_max = max_subarray_sum(arr, mid + 1, right)
    # Maximum subarray sum crossing the midpoint
    cross_max = max_crossing_sum(arr, left, mid, right)
    return max(left_max, right_max, cross_max)

# Driver code
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_subarray_sum(arr, 0, n - 1))
