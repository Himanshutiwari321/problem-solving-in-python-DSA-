# maximum sum of subarray size k 

nums = [1,12,-5,-6,50,3]
k = 4
n = len(nums)
sums =0
left = 0 
right = 0
max_arr = float('-inf') # max_arr initilize from nagative because might be nagative value in array that's why we cannot initilize with 0

while right < n:
    sums = sums + nums[right]
    if right-left+1 < k :
       right+=1

    elif right - left + 1 == k:
        max_arr = max(max_arr , sums)
        sums = sums - nums[left]
        left+=1
        right+=1

print(max_arr//k)
print(max_arr/float(k))
print(max_arr) 
print(max_arr//float(k))         