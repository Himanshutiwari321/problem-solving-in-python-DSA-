#range sum query - immutable 
nums = [-2, 0, 3, -5, 2, -1]
queries = [[0, 2], [2, 5], [0, 5]]

n = len (nums)
result = [0]*(n+1)
prefix  = 0

for i in range (n):
    prefix = prefix + nums[i]
    result[i+1]= prefix

for q in queries:
    left , right = q 
    print(result[right + 1] - result[left] )   

