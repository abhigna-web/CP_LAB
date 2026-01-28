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
1
3 50
60 10
100 20
120 30
#Expected Output
240.000000
