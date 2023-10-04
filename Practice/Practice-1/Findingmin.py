arr = list(map(int,"10 200 100 300 1000 30 20 ".split()))
k = 3
print(arr)
arr.sort()
print(arr)
temp = arr[:k]
max_ele = max(temp)
min_ele = min(temp)
print(max_ele-min_ele)